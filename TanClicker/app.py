import asyncio
import flet as ft


async def main(page: ft.Page) -> None:
    page.title = "Tan Clicker"
    page.theme_mode =  ft.ThemeMode.DARK
    page.bgcolor = "#000000"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts ={"Fulbo_Argenta": "fonts/Fulbo_Argenta.ttf"}
    page.theme = ft.Theme(font_family="Fulbo_Argenta")

    def on_tap_down(event: ft.ContainerTapEvent):
            global tap_position
            tap_position = (event.local_x, event.local_y)

    async def score_up(event: ft.ContainerTapEvent) -> None:
        score.data += 1
        score.value = str(score.data)

        image.scale = 0.95
        
        score_counter.opacity = 100
        score_counter.value = "+1"
        score_counter.right = 0
        score_counter.left = tap_position[0]
        score_counter.top = tap_position[1]
        score_counter.bottom = 0

        await page.update_async()

        await asyncio.sleep(0.1)
        image.scale = 1
        score_counter.opacity = 0

        await page.update_async()



    score = ft.Text(value="0", size=100, data=0)
    score_counter = ft.Text(
        size= 50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )
    image = ft.Image(
        src="anime7.jpg",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )


    await page.add_async(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            on_tap_down=on_tap_down,
            margin=ft.Margin(0,0,0,30)
            )
    )

if __name__ =="__main__":
    tap_position = (0, 0)
    ft.app(target=main, view=ft.WEB_BROWSER)