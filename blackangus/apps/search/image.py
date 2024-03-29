import logging
from typing import Optional, Dict, Any, Tuple

from discord import Client, Message, Embed, Color

from blackangus.apps.base import PresentedResponseApp
from blackangus.apps.search.base import parse_search_command
from blackangus.config import Config
from blackangus.models.search import GoogleImagesModel
from blackangus.scrapper.google_images import GoogleImagesScrapper


class GoogleImageSearchApp(PresentedResponseApp):
    disabled = False
    commands = ['image', '짤']

    def __init__(self, config: Config, client: Client):
        self.config = config
        self.client = client

    async def parse_command(self, context: Message) -> Optional[Dict[str, Any]]:
        return await parse_search_command(context)

    @staticmethod
    def help_embed() -> Embed:
        return Embed(
            title='Google Images 검색',
            description='흑우로 구글 이미지를 검색할 수 있습니다. API 방식이 아닌 스크래핑 방식을 이용하며, '
            '비-로그인 상태 웹에서 보는 것과 동일한 결과를 얻을 수 있습니다.\n'
            '사용법은 `!image --count=갯수 검색어`로 입력하면 되며, 30개 이하의 결과만 가져올 수 있습니다.\n'
            '사진이 너무 많으면 도배가 될 수 있으니 사용에 주의하세요. `--count` 옵션이 없으면 기본은 1개입니다.',
            color=Color.red(),
        )

    @staticmethod
    def result_to_embed(model: GoogleImagesModel) -> Embed:
        logging.info(
            f'[GoogleImagesModel] {model.title} / {model.destination_link} / {model.image_link}'
        )
        return Embed(
            title=f'{model.title}',
            color=Color.green(),
            url=model.destination_link,
        ).set_image(url=model.image_link)

    @staticmethod
    def error_embed(error: Exception) -> Embed:
        return Embed(
            title='구글 검색 오류',
            description='구글 검색 중 오류가 발생했습니다.\n' f'{error}',
            color=Color.red(),
        )

    async def present(
        self, command: Dict[str, Any]
    ) -> Tuple[Optional[str], Optional[Embed]]:
        if command.get('help', False):
            return None, self.help_embed()

        keyword = command['keyword']
        scrapper = GoogleImagesScrapper()

        try:
            await scrapper.initialize()
            results = await scrapper.scrape(keyword, command['count'])
            await scrapper.finalize()

            if len(results) == 0:
                return '검색 결과가 없습니다.', None

            embeds = map(lambda result: self.result_to_embed(result), results)
            channel = self.client.get_channel(command['channel'])

            await channel.send(content='구글 이미지 검색 결과입니다.')
            for embed in embeds:
                await channel.send(embed=embed)
        except Exception as e:
            return None, self.error_embed(e)

        return None, None
