import flet as ft

ticket_prices = [
    # Nangang, Taipei, Banqiao, Taoyuan, Hsinchu, Miaoli, Taichung, Changhua, Yunlin, Chiayi, Tainan, Zuoying
    ["-", 260, 310, 500, 700, 920, 1330, 1510, 1660, 1880, 2290, 2500],  # Nangang
    [40, "-", 260, 440, 640, 850, 1250, 1430, 1600, 1820, 2230, 2440],  # Taipei
    [70, 40, "-", 400, 590, 800, 1210, 1390, 1550, 1780, 2180, 2390],  # Banqiao
    [200, 160, 130, "-", 400, 620, 1010, 1210, 1370, 1580, 1990, 2200],  # Taoyuan
    [330, 290, 260, 130, "-", 410, 820, 1010, 1160, 1390, 1790, 2000],  # Hsinchu
    [480, 430, 400, 280, 140, "-", 610, 790, 950, 1160, 1580, 1790],  # Miaoli
    [750, 700, 670, 540, 410, 270, "-", 400, 550, 770, 1180, 1390],  # Taichung
    [870, 820, 790, 670, 540, 390, 130, "-", 370, 580, 1000, 1210],  # Changhua
    [970, 930, 900, 780, 640, 500, 230, 110, "-", 430, 830, 1040],  # Yunlin
    [1120, 1080, 1050, 920, 790, 640, 380, 250, 150, "-", 620, 820],  # Chiayi
    [1390, 1350, 1320, 1190, 1060, 920, 650, 530, 420, 280, "-", 410],  # Tainan
    [1530, 1490, 1460, 1330, 1200, 1060, 790, 670, 560, 410, 140, "-"]   # Zuoying
]

def main(page: ft.Page):
    page.title = "Taiwan Hign Speed Rail Fare System"
    #建立按鈕
    def go_start ( e ) :
        global start_station_num 
        start_station_num = int(  e.control.data  ) 
        show_start.value = f"The start station you choice : { e.control.text }" 
        page.update() 

    def go_end ( e ) :
        global end_station_num 
        end_station_num = int(  e.control.data  ) 
        show_end.value = f"The end station you choice : { e.control.text }"  
        page.update() 

    def go_Dutch ( e ) :
       standard_fare = ticket_prices[ start_station_num ][ end_station_num ]
       #business_fare = ticket_prices[ start_station_num ][ end_station_num ]
       business_fare = ticket_prices[ end_station_num ][ start_station_num ]
       if standard_fare > business_fare :
           standard_fare , business_fare = business_fare , standard_fare
           #因為將題目誤解為車站不同而有票價差別，故用防呆機制解決問題，就是選擇貴的當作商務車票
       show_standard_fare.value = f"The ticket fare of Standard car is : {standard_fare}"  #show_fare.value
       show_business_fare.value = f"The ticket fare of Business car is : {business_fare}"  #show_fare.value
       page.update()


    #建立部件
    start_hint = ft.Text( value="Please select a start station" , size = "12" )
    end_hint = ft.Text( value="Please select a end station" , size = "12" )
    fare_button = ft.ElevatedButton( text="Calculate the fare" , on_click=go_Dutch )
    show_start = ft.Text( value="", size = 12 )
    show_end = ft.Text( value="", size = 12 )
    show_standard_fare = ft.Text( value="", size = 12 )
    show_business_fare = ft.Text( value="", size = 12 )

    #start
    Nangang_button_start = ft.ElevatedButton( data = 0, text="Nangang" , on_click= go_start )
    Taipei_button_start = ft.ElevatedButton( data = 1,text="Taipei", on_click= go_start )
    Banqiao_button_start = ft.ElevatedButton( data = 2, text="Banqiao", on_click= go_start )
    Taoyuan_button_start = ft.ElevatedButton( data = 3, text="Taoyuan", on_click= go_start )
    Hsinchu_button_start = ft.ElevatedButton( data = 4, text="Hsinchu", on_click= go_start )
    Miaoli_button_start = ft.ElevatedButton( data = 5, text="Miaoli", on_click= go_start )
    Taichung_button_start = ft.ElevatedButton( data = 6, text="Taichung", on_click= go_start )
    Changhua_button_start = ft.ElevatedButton( data = 7, text="Changhua", on_click= go_start )
    Yunlin_button_start = ft.ElevatedButton( data = 8, text="Yunlin", on_click= go_start )
    Chiayi_button_start = ft.ElevatedButton( data = 9, text="Chiayi", on_click= go_start )
    Tainan_button_start = ft.ElevatedButton( data = 10, text="Tainan", on_click= go_start )
    Zuoying_button_start = ft.ElevatedButton( data = 11, text="Zuoying", on_click= go_start )

    #end
    Nangang_button_end = ft.ElevatedButton( data = 0, text="Nangang" , on_click= go_end )
    Taipei_button_end = ft.ElevatedButton( data = 1,text="Taipei", on_click= go_end )
    Banqiao_button_end = ft.ElevatedButton( data = 2, text="Banqiao", on_click= go_end )
    Taoyuan_button_end = ft.ElevatedButton( data = 3, text="Taoyuan", on_click= go_end )
    Hsinchu_button_end = ft.ElevatedButton( data = 4, text="Hsinchu", on_click= go_end )
    Miaoli_button_end = ft.ElevatedButton( data = 5, text="Miaoli", on_click= go_end )
    Taichung_button_end = ft.ElevatedButton( data = 6, text="Taichung", on_click= go_end )
    Changhua_button_end = ft.ElevatedButton( data = 7, text="Changhua", on_click= go_end )
    Yunlin_button_end = ft.ElevatedButton( data = 8, text="Yunlin", on_click= go_end )
    Chiayi_button_end = ft.ElevatedButton( data = 9, text="Chiayi", on_click= go_end )
    Tainan_button_end = ft.ElevatedButton( data = 10, text="Tainan", on_click= go_end )
    Zuoying_button_end = ft.ElevatedButton( data = 11, text="Zuoying", on_click= go_end )

    start_station = ft.Column(
        [
            ft.Row(  [Nangang_button_start ,  Taipei_button_start ,  Banqiao_button_start ,  Taoyuan_button_start ], alignment=ft.MainAxisAlignment.CENTER ),
            ft.Row(  [Hsinchu_button_start ,  Miaoli_button_start ,  Taichung_button_start , Changhua_button_start] , alignment=ft.MainAxisAlignment.CENTER ),
            ft.Row(  [Yunlin_button_start ,  Chiayi_button_start ,  Tainan_button_start , Zuoying_button_start] , alignment=ft.MainAxisAlignment.CENTER ),
        ],
        alignment = ft.MainAxisAlignment.CENTER
    )
    end_station = ft.Column(
        [
            ft.Row( [ Nangang_button_end ,  Taipei_button_end ,  Banqiao_button_end ,  Taoyuan_button_end ], alignment=ft.MainAxisAlignment.CENTER ),
            ft.Row( [ Hsinchu_button_end ,  Miaoli_button_end ,  Taichung_button_end ,  Changhua_button_end ], alignment=ft.MainAxisAlignment.CENTER ),
            ft.Row( [ Yunlin_button_end ,  Chiayi_button_end , Tainan_button_end ,  Zuoying_button_end ], alignment=ft.MainAxisAlignment.CENTER ),
        ],
        alignment = ft.MainAxisAlignment.CENTER
    )
    
    page.add(
        ft.Column(
        [   ft.Row([ start_hint ], alignment = ft.MainAxisAlignment.CENTER ),
            ft.Row([ start_station ], alignment = ft.MainAxisAlignment.CENTER ),
            ft.Row([ end_hint ], alignment = ft.MainAxisAlignment.CENTER),
            ft.Row([ end_station ], alignment = ft.MainAxisAlignment.CENTER ),
            ft.Row([ fare_button ], alignment = ft.MainAxisAlignment.CENTER),
            ft.Row([ show_start ], alignment = ft.MainAxisAlignment.CENTER),
            ft.Row([ show_end ], alignment = ft.MainAxisAlignment.CENTER),
            ft.Row([ show_standard_fare ], alignment = ft.MainAxisAlignment.CENTER),
            ft.Row([ show_business_fare ], alignment = ft.MainAxisAlignment.CENTER),
        ], alignment = ft.MainAxisAlignment.CENTER
        )
    )

ft.app( target = main )
 