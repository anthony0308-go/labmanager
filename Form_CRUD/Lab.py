import flet as ft

class Form(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)
        
        self.mode_switch = ft.Switch(
            value=True,
            on_change=self.mode_change_update,
            thumb_color="Black",
            thumb_icon={
                ft.MaterialState.DEFAULT: ft.icons.LIGHT_MODE,
                ft.MaterialState.SELECTED: ft.icons.DARK_MODE
            }
        )

        self.nav = ft.Container(
            col=1,
            bgcolor="#960000",
            border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        expand=True,
                        content=ft.NavigationRail(
                            bgcolor="#960000",
                            expand=True,
                            selected_index=0,
                            destinations=[
                                ft.NavigationDestination(
                                    icon_content=ft.Icon(ft.icons.HOME, color="white"),
                                    selected_icon_content=ft.Icon(ft.icons.HOME, color="white"),
                                ),
                                ft.NavigationDestination(
                                    icon_content=ft.Icon(ft.icons.CALENDAR_MONTH_SHARP, color="white"),
                                    selected_icon_content=ft.Icon(ft.icons.CALENDAR_MONTH_SHARP, color="white"),
                                ),
                                ft.NavigationDestination(
                                    icon_content=ft.Icon(ft.icons.SETTINGS, color="white"),
                                    selected_icon_content=ft.Icon(ft.icons.SETTINGS, color="white"),
                                ),
                            ]
                        )
                    ),
                    ft.Container(
                        expand=True,
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            expand=True,
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.OUTPUT,
                                    icon_color="white"
                                ),
                                self.mode_switch
                            ],
                        )
                    ),
                ]
            )
        )

        self.form = ft.Container(
            bgcolor="#222222",
            border_radius=10,
            col=4,
        )

        self.table = ft.Container(
            bgcolor="#222222",
            border_radius=10,
            col=7,
        )

        self.content = ft.ResponsiveRow(
            controls=[
                self.nav,
                self.form,
                self.table,
            ]
        )

    def mode_change_update(self, e):
        if e.control.value:
            self.page.theme_mode = "dark"
        else:
            self.page.theme_mode = "light"
        self.page.update()

    def build(self):
        return self.content
        

def main(page: ft.Page):
    page.title = "Organizador de Laboratorio"
    page.add(Form())
    
ft.app(main)  # , view=ft.WEB_BROWSER
