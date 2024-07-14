from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

class News:
    def __init__(self, tit, des, img):
        self.tit = tit
        self.des = des
        self.img = img


# Create news objects
news1 = News("Iphone 14 Pro",
             "iPhone 14 Pro and iPhone 14 Pro Max are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529(maximum depth of 6 meters up to 30 minutes.",
             "https://netrinoimages.s3.eu-west-2.amazonaws.com/2022/12/08/1373191/426752/iphone_14_pro_max_3d_model_c4d_max_obj_fbx_ma_lwo_3ds_3dm_stl_4402727_o.png")
news2 = News("New iPadOS 17",
             "iPadOS 17 takes iPad even further. With new levels of personalization, beautiful and helpful custom Lock Screens, and features to help you get more done, iPad is more capable than ever.",
             "https://b2c-contenthub.com/wp-content/uploads/2023/06/iPadOS-17-lock-screen-customization.jpg?quality=50&strip=all&w=1200")
news3 = News("New General AI",
             "The ultimate achievement to some in the AI industry is creating a system with artificial general intelligence (AGI), or the ability to understand and learn any task that a human can.",
             "https://rare-gallery.com/thumbs/1170002-white-digital-art-simple-background-robot-vehicle-sculpture-technology-Toy-machine-artificial-intelligence-Hi-Tech-hand-product.jpg")
news4 = News("Samsung S22 Ultra",
             "The iconic S Pen fits right into S for the first time. Eject it from the bottom to take notes, sketch, edit content with precision or control your phone.",
             "https://cdn.dxomark.com/wp-content/uploads/medias/post-112004/Samsung-Galaxy-S22-Ultra-Snapdragon_Yoast-image-packshot-review-Recovered-1.jpg")
news5 = News("Redmi Note 12 Pro 5G",
             "Powerful AI algorithms greatly improve image quality and speed. Every priceless moment in your life comes to life, waiting for you to seize.",
             "https://i0.wp.com/www.xiaomiboutique.com/wp-content/uploads/2023/05/Redmi-Note-12-Pro-5G_pms_1679660364.87997620.png?fit=1600%2C1600&ssl=1")
news6 = News("iPhone 12 Pro Max",
             "The iPhone 12 Pro Max display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 6.68 inches diagonally (actual viewable area is less).",
             "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/refurb-iphone-12-pro-max-gold-2020?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1635202937000")
news7 = News("Iphone 14 Pro",
             "iPhone 14 Pro and iPhone 14 Pro Max are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529(maximum depth of 6 meters up to 30 minutes.",
             "https://netrinoimages.s3.eu-west-2.amazonaws.com/2022/12/08/1373191/426752/iphone_14_pro_max_3d_model_c4d_max_obj_fbx_ma_lwo_3ds_3dm_stl_4402727_o.png")
news8 = News("New iPadOS 17",
             "iPadOS 17 takes iPad even further. With new levels of personalization, beautiful and helpful custom Lock Screens, and features to help you get more done, iPad is more capable than ever.",
             "https://b2c-contenthub.com/wp-content/uploads/2023/06/iPadOS-17-lock-screen-customization.jpg?quality=50&strip=all&w=1200")
news9 = News("New General AI",
             "The ultimate achievement to some in the AI industry is creating a system with artificial general intelligence (AGI), or the ability to understand and learn any task that a human can.",
             "https://rare-gallery.com/thumbs/1170002-white-digital-art-simple-background-robot-vehicle-sculpture-technology-Toy-machine-artificial-intelligence-Hi-Tech-hand-product.jpg")
news10 = News("Samsung S22 Ultra",
             "The iconic S Pen fits right into S for the first time. Eject it from the bottom to take notes, sketch, edit content with precision or control your phone.",
             "https://cdn.dxomark.com/wp-content/uploads/medias/post-112004/Samsung-Galaxy-S22-Ultra-Snapdragon_Yoast-image-packshot-review-Recovered-1.jpg")
news11 = News("Redmi Note 12 Pro 5G",
             "Powerful AI algorithms greatly improve image quality and speed. Every priceless moment in your life comes to life, waiting for you to seize.",
             "https://i0.wp.com/www.xiaomiboutique.com/wp-content/uploads/2023/05/Redmi-Note-12-Pro-5G_pms_1679660364.87997620.png?fit=1600%2C1600&ssl=1")
news12 = News("iPhone 12 Pro Max",
             "The iPhone 12 Pro Max display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 6.68 inches diagonally (actual viewable area is less).",
             "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/refurb-iphone-12-pro-max-gold-2020?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1635202937000")
news13 = News("Iphone 14 Pro",
             "iPhone 14 Pro and iPhone 14 Pro Max are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529(maximum depth of 6 meters up to 30 minutes.",
             "https://netrinoimages.s3.eu-west-2.amazonaws.com/2022/12/08/1373191/426752/iphone_14_pro_max_3d_model_c4d_max_obj_fbx_ma_lwo_3ds_3dm_stl_4402727_o.png")
news14 = News("New iPadOS 17",
             "iPadOS 17 takes iPad even further. With new levels of personalization, beautiful and helpful custom Lock Screens, and features to help you get more done, iPad is more capable than ever.",
             "https://b2c-contenthub.com/wp-content/uploads/2023/06/iPadOS-17-lock-screen-customization.jpg?quality=50&strip=all&w=1200")
news15 = News("New General AI",
             "The ultimate achievement to some in the AI industry is creating a system with artificial general intelligence (AGI), or the ability to understand and learn any task that a human can.",
             "https://rare-gallery.com/thumbs/1170002-white-digital-art-simple-background-robot-vehicle-sculpture-technology-Toy-machine-artificial-intelligence-Hi-Tech-hand-product.jpg")
news16 = News("Samsung S22 Ultra",
             "The iconic S Pen fits right into S for the first time. Eject it from the bottom to take notes, sketch, edit content with precision or control your phone.",
             "https://cdn.dxomark.com/wp-content/uploads/medias/post-112004/Samsung-Galaxy-S22-Ultra-Snapdragon_Yoast-image-packshot-review-Recovered-1.jpg")
news17 = News("Redmi Note 12 Pro 5G",
             "Powerful AI algorithms greatly improve image quality and speed. Every priceless moment in your life comes to life, waiting for you to seize.",
             "https://i0.wp.com/www.xiaomiboutique.com/wp-content/uploads/2023/05/Redmi-Note-12-Pro-5G_pms_1679660364.87997620.png?fit=1600%2C1600&ssl=1")
news18 = News("iPhone 12 Pro Max",
             "The iPhone 12 Pro Max display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 6.68 inches diagonally (actual viewable area is less).",
             "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/refurb-iphone-12-pro-max-gold-2020?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1635202937000")
news19 = News("Iphone 14 Pro",
             "iPhone 14 Pro and iPhone 14 Pro Max are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529(maximum depth of 6 meters up to 30 minutes.",
             "https://netrinoimages.s3.eu-west-2.amazonaws.com/2022/12/08/1373191/426752/iphone_14_pro_max_3d_model_c4d_max_obj_fbx_ma_lwo_3ds_3dm_stl_4402727_o.png")
news20 = News("New iPadOS 17",
             "iPadOS 17 takes iPad even further. With new levels of personalization, beautiful and helpful custom Lock Screens, and features to help you get more done, iPad is more capable than ever.",
             "https://b2c-contenthub.com/wp-content/uploads/2023/06/iPadOS-17-lock-screen-customization.jpg?quality=50&strip=all&w=1200")
news21 = News("New General AI",
             "The ultimate achievement to some in the AI industry is creating a system with artificial general intelligence (AGI), or the ability to understand and learn any task that a human can.",
             "https://rare-gallery.com/thumbs/1170002-white-digital-art-simple-background-robot-vehicle-sculpture-technology-Toy-machine-artificial-intelligence-Hi-Tech-hand-product.jpg")
news22 = News("Samsung S22 Ultra",
             "The iconic S Pen fits right into S for the first time. Eject it from the bottom to take notes, sketch, edit content with precision or control your phone.",
             "https://cdn.dxomark.com/wp-content/uploads/medias/post-112004/Samsung-Galaxy-S22-Ultra-Snapdragon_Yoast-image-packshot-review-Recovered-1.jpg")
news23 = News("Redmi Note 12 Pro 5G",
             "Powerful AI algorithms greatly improve image quality and speed. Every priceless moment in your life comes to life, waiting for you to seize.",
             "https://i0.wp.com/www.xiaomiboutique.com/wp-content/uploads/2023/05/Redmi-Note-12-Pro-5G_pms_1679660364.87997620.png?fit=1600%2C1600&ssl=1")
news24 = News("iPhone 12 Pro Max",
             "The iPhone 12 Pro Max display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 6.68 inches diagonally (actual viewable area is less).",
             "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/refurb-iphone-12-pro-max-gold-2020?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1635202937000")


# Store news objects in a list
news_list = [news1, news2, news3, news4, news5, news6, news7, news8, news9, news10, news11, news12, news13, news14, news15, news16, news17, news18, news19, news20, news21, news22, news23, news24]


@app.route('/api/news', methods=['GET'])
@cross_origin()
def get_news():

    news_data = []
    for news in news_list:
        news_data.append({
            'tit': news.tit,
            'des': news.des,
            'img': news.img
        })

    return jsonify({'news': news_data})


if __name__ == '__main__':
    app.run(debug=True)