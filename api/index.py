from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

API_KEY = '1234567890abcdef1234567890abcmnb'

class News:
    def __init__(self, tit, des, img):
        self.tit = tit
        self.des = des
        self.img = img


# Create news objects
news1 = News("iPhone 16 Pro Max",
             "The iPhone 16 Pro Max will feature a larger 6.9-inch display, powered by the A18 Pro chip with enhanced AI capabilities, and will include a new dedicated Capture button for improved camera functionality.",
             "https://picsum.photos/400?random=2")
news2 = News("AirPods Pro 3",
             "The AirPods Pro 3 are expected to feature new adaptive audio technology, improved noise cancellation, and potentially offer new color options. They are still in early development stages.",
             "https://picsum.photos/400?random=3")
news3 = News("Apple Watch Ultra 3",
             "The Apple Watch Ultra 3 will likely maintain the same rugged design as its predecessor but may include new health features like blood pressure monitoring and sleep apnea detection, alongside minor hardware upgrades.",
             "https://picsum.photos/400?random=4")
news4 = News("iPad Pro 2025",
             "The iPad Pro 2025 might feature an OLED display with thinner bezels, powered by the M3 chip, offering enhanced performance and longer battery life.",
             "https://picsum.photos/400?random=5")
news5 = News("MacBook Pro 2025",
             "The MacBook Pro 2025 is expected to include an M3 Max chip, providing faster processing, a Mini-LED display, and improved thermal management.",
             "https://picsum.photos/400?random=6")
news6 = News("Apple Vision Pro 2",
             "Apple Vision Pro 2 is anticipated to enhance augmented reality experiences with a slimmer design, better battery life, and more immersive display technology.",
             "https://picsum.photos/400?random=7")
news7 = News("iPhone 16 Pro Max",
             "The iPhone 16 Pro Max will feature a larger 6.9-inch display, powered by the A18 Pro chip with enhanced AI capabilities, and will include a new dedicated Capture button for improved camera functionality.",
             "https://picsum.photos/400?random=8")
news8 = News("AirPods Pro 3",
             "The AirPods Pro 3 are expected to feature new adaptive audio technology, improved noise cancellation, and potentially offer new color options. They are still in early development stages.",
             "https://picsum.photos/400?random=9")
news9 = News("Apple Watch Ultra 3",
             "The Apple Watch Ultra 3 will likely maintain the same rugged design as its predecessor but may include new health features like blood pressure monitoring and sleep apnea detection, alongside minor hardware upgrades.",
             "https://picsum.photos/400?random=10")
news10 = News("iPad Pro 2025",
             "The iPad Pro 2025 might feature an OLED display with thinner bezels, powered by the M3 chip, offering enhanced performance and longer battery life.",
             "https://picsum.photos/400?random=11")
news11 = News("MacBook Pro 2025",
             "The MacBook Pro 2025 is expected to include an M3 Max chip, providing faster processing, a Mini-LED display, and improved thermal management.",
             "https://picsum.photos/400?random=12")
news12 = News("Apple Vision Pro 2",
             "Apple Vision Pro 2 is anticipated to enhance augmented reality experiences with a slimmer design, better battery life, and more immersive display technology.",
             "https://picsum.photos/400?random=13")
news13 = News("iPhone 16 Pro Max",
             "The iPhone 16 Pro Max will feature a larger 6.9-inch display, powered by the A18 Pro chip with enhanced AI capabilities, and will include a new dedicated Capture button for improved camera functionality.",
             "https://picsum.photos/400?random=14")
news14 = News("AirPods Pro 3",
             "The AirPods Pro 3 are expected to feature new adaptive audio technology, improved noise cancellation, and potentially offer new color options. They are still in early development stages.",
             "https://picsum.photos/400?random=15")
news15 = News("Apple Watch Ultra 3",
             "The Apple Watch Ultra 3 will likely maintain the same rugged design as its predecessor but may include new health features like blood pressure monitoring and sleep apnea detection, alongside minor hardware upgrades.",
             "https://picsum.photos/400?random=16")
news16 = News("iPad Pro 2025",
             "The iPad Pro 2025 might feature an OLED display with thinner bezels, powered by the M3 chip, offering enhanced performance and longer battery life.",
             "https://picsum.photos/400?random=17")
news17 = News("MacBook Pro 2025",
             "The MacBook Pro 2025 is expected to include an M3 Max chip, providing faster processing, a Mini-LED display, and improved thermal management.",
             "https://picsum.photos/400?random=18")
news18 = News("Apple Vision Pro 2",
             "Apple Vision Pro 2 is anticipated to enhance augmented reality experiences with a slimmer design, better battery life, and more immersive display technology.",
             "https://picsum.photos/400?random=19")
news19 = News("iPhone 16 Pro Max",
             "The iPhone 16 Pro Max will feature a larger 6.9-inch display, powered by the A18 Pro chip with enhanced AI capabilities, and will include a new dedicated Capture button for improved camera functionality.",
             "https://picsum.photos/400?random=20")
news20 = News("AirPods Pro 3",
             "The AirPods Pro 3 are expected to feature new adaptive audio technology, improved noise cancellation, and potentially offer new color options. They are still in early development stages.",
             "https://picsum.photos/400?random=21")
news21 = News("Apple Watch Ultra 3",
             "The Apple Watch Ultra 3 will likely maintain the same rugged design as its predecessor but may include new health features like blood pressure monitoring and sleep apnea detection, alongside minor hardware upgrades.",
             "https://picsum.photos/400?random=22")
news22 = News("iPad Pro 2025",
             "The iPad Pro 2025 might feature an OLED display with thinner bezels, powered by the M3 chip, offering enhanced performance and longer battery life.",
             "https://picsum.photos/400?random=23")
news23 = News("MacBook Pro 2025",
             "The MacBook Pro 2025 is expected to include an M3 Max chip, providing faster processing, a Mini-LED display, and improved thermal management.",
             "https://picsum.photos/400?random=24")
news24 = News("Apple Vision Pro 2",
             "Apple Vision Pro 2 is anticipated to enhance augmented reality experiences with a slimmer design, better battery life, and more immersive display technology.",
             "https://picsum.photos/400?random=25")


# Store news objects in a list
news_list = [news1, news2, news3, news4, news5, news6, news7, news8, news9, news10, news11, news12, news13, news14, news15, news16, news17, news18, news19, news20, news21, news22, news23, news24]

def require_api_key(view_function):
    def decorated_function(*args, **kwargs):
        api_key = request.args.get('api_key')
        if api_key and api_key == API_KEY:
            return view_function(*args, **kwargs)
        else:
            abort(401)  # Unauthorized
    return decorated_function

@app.route('/api/news', methods=['GET'])
@cross_origin()
@require_api_key
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