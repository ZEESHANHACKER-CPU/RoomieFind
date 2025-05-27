from flask import Flask, request, render_template, jsonify, flash, redirect, url_for
import os
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Mock Roommate listings 
roommate_listings = [
    {
        "name": "Alina",
        "social_class": "Middle",
        "price_range": "15000",
        "hobby": "Reading",
        "city": "Islamabad",
        "gender": "Female",
        "image_url": "https://images.unsplash.com/photo-1607746882042-944635dfe10e"
    },
    {
        "name": "Alia",
        "social_class": "Upper",
        "price_range": "20000",
        "hobby": "Sports",
        "city": "Lahore",
        "gender": "Female",
        "image_url": "https://images.unsplash.com/photo-1544005313-94ddf0286df2"
    },
    {
        "name": "Umer",
        "social_class": "Lower",
        "price_range": "25000",
        "hobby": "Gaming",
        "city": "Karachi",
        "gender": "Male",
        "image_url": "https://images.unsplash.com/photo-1531123897727-8f129e1688ce"
    },
    {
        "name": "Sara",
        "social_class": "Middle",
        "price_range": "15000",
        "hobby": "Reading",
        "city": "Islamabad",
        "gender": "Female",
        "image_url": "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e"
    },
    {
        "name": "Ahmed",
        "social_class": "Upper",
        "price_range": "20000",
        "hobby": "Sports",
        "city": "Lahore",
        "gender": "Male",
        "image_url": "https://images.unsplash.com/photo-1502767089025-6572583495b0"
    },
    {
        "name": "Fatima",
        "social_class": "Lower",
        "price_range": "25000",
        "hobby": "Gaming",
        "city": "Karachi",
        "gender": "Female",
        "image_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d"
    },
    {
        "name": "Bilal",
        "social_class": "Middle",
        "price_range": "15000",
        "hobby": "Reading",
        "city": "Islamabad",
        "gender": "Male",
        "image_url": "https://images.unsplash.com/photo-1527980965255-d3b416303d12"
    },
    {
        "name": "Ayesha",
        "social_class": "Upper",
        "price_range": "20000",
        "hobby": "Sports",
        "city": "Lahore",
        "gender": "Female",
        "image_url": "https://images.unsplash.com/photo-1545992336-0ed8c6a9f8f4"
    },
    {
        "name": "Hassan",
        "social_class": "Lower",
        "price_range": "25000",
        "hobby": "Gaming",
        "city": "Karachi",
        "gender": "Male",
        "image_url": "https://images.unsplash.com/photo-1629112022322-0b60e2ed2025"
    },
    {
        "name": "Zara",
        "social_class": "Middle",
        "price_range": "15000",
        "hobby": "Reading",
        "city": "Islamabad",
        "gender": "Female",
        "image_url": "https://images.unsplash.com/photo-1517841905240-472988babdf9"
    },
    
    {"name": "Mariam", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/1.jpg"},
    {"name": "Usman", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/1.jpg"},
    {"name": "Sana", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/2.jpg"},
    {"name": "Tariq", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/2.jpg"},
    {"name": "Nida", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/3.jpg"},
    {"name": "Kamran", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/3.jpg"},
    {"name": "Rabia", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/4.jpg"},
    {"name": "Faisal", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/4.jpg"},
    {"name": "Hina", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/5.jpg"},
    {"name": "Shahid", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/5.jpg"},
    {"name": "Lubna", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/6.jpg"},
    {"name": "Omar", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/6.jpg"},
    {"name": "Sadia", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/7.jpg"},
    {"name": "Junaid", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/7.jpg"},
    {"name": "Mehwish", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/8.jpg"},
    {"name": "Asad", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/8.jpg"},
    {"name": "Naveed", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/9.jpg"},
    {"name": "Samina", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/9.jpg"},
    {"name": "Yasir", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/10.jpg"},
    {"name": "Adeel", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/11.jpg"},
    {"name": "Noreen", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/10.jpg"},
    {"name": "Saad", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/12.jpg"},
    {"name": "Amina", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/11.jpg"},
    {"name": "Zeeshan", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/13.jpg"},
    {"name": "Hafsa", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/12.jpg"},
    {"name": "Farhan", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/14.jpg"},
    {"name": "Iqra", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/13.jpg"},
    {"name": "Rizwan", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/15.jpg"},
    {"name": "Shazia", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/14.jpg"},
    {"name": "Talha", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/16.jpg"},
    {"name": "Bushra", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/15.jpg"},
    {"name": "Waqas", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/17.jpg"},
    {"name": "Sahar", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/16.jpg"},
    {"name": "Danish", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/18.jpg"},
    {"name": "Mahnoor", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/17.jpg"},
    {"name": "Jibran", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/19.jpg"},
    {"name": "Sumbal", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/18.jpg"},
    {"name": "Faizan", "social_class": "Middle", "price_range": "15000", "hobby": "Reading", "city": "Islamabad", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/20.jpg"},
    {"name": "Nashit", "social_class": "Upper", "price_range": "20000", "hobby": "Sports", "city": "Lahore", "gender": "Male", "image_url": "https://randomuser.me/api/portraits/men/21.jpg"},
 
    {"name": "Hoor", "social_class": "Lower", "price_range": "25000", "hobby": "Gaming", "city": "Karachi", "gender": "Female", "image_url": "https://randomuser.me/api/portraits/women/19.jpg"}
]

# Room listings
rooms = [
  {
    "id": 1,
    "title": "Cozy Studio in Downtown",
    "price": 15000,
    "city": "Islamabad",
    "image": "https://images.unsplash.com/photo-1560448075-345a58f2a04b?auto=format&fit=crop&w=800&q=80"
  },
  {
    "id": 2,
    "title": "Modern Room Near Park",
    "price": 20000,
    "city": "Lahore",
    "image": "https://images.unsplash.com/photo-1505692794403-9b3bce9ec1a3?auto=format&fit=crop&w=800&q=80"
  },
  {
    "id": 3,
    "title": "Bright & Spacious Room",
    "price": 25000,
    "city": "Karachi",
    "image": "https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=800&q=80"
  },
  {
    "id": 4,
    "title": "Minimalist Room with Balcony",
    "price": 15000,
    "city": "Islamabad",
    "image": "https://images.unsplash.com/photo-1549187774-b4e9a0b7c4e3?auto=format&fit=crop&w=800&q=80"
  },
  {
    "id": 5,
    "title": "Comfortable Room with City View",
    "price": 20000,
    "city": "Lahore",
    "image": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=800&q=80"
  },
  {
    "id": 6,
    "title": "Charming Room Near University",
    "price": 18000,
    "city": "Karachi",
    "image": "https://images.unsplash.com/photo-1554995207-c18c203602cb?auto=format&fit=crop&w=800&q=80"
  },
  {
    "id": 7,
    "title": "Sunny Room with Large Windows",
    "price": 16000,
    "city": "Islamabad",
    "image": "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?auto=format&fit=crop&w=800&q=80"
  },
  {
    "id": 8,
    "title": "Quiet Room in Safe Neighborhood",
    "price": 17000,
    "city": "Lahore",
    "image": "https://images.unsplash.com/photo-1472220625704-91e1462799b2?auto=format&fit=crop&w=800&q=80"
  },
  {
    "id": 9,
    "title": "Modern Apartment Room",
    "price": 22000,
    "city": "Karachi",
    "image": "https://images.unsplash.com/photo-1501183638714-3c2723f0a1bb?auto=format&fit=crop&w=800&q=80"
  }
]

@app.route('/')
def home():
    return render_template('index.html')

# Form to create a new listing
@app.route('/new-listing')
def new_listing():
    return render_template('new_listing.html')

# Redirect to quiz form
@app.route('/find-listing')
def find_listing():
    return redirect(url_for('quiz'))

# Quiz page: GET to display form, POST to process form
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'GET':
        return render_template('quiz.html')

    # Extract form data
    listing_type = request.form.get('listingType')
    social_class = request.form.get('socialClass')
    price_range = request.form.get('priceRange')
    hobby = request.form.get('hobby')
    city = request.form.get('city')

    # Validate listing type
    if not listing_type:
        flash("Please select a listing type.", "error")
        return redirect(url_for('quiz'))

    matched_listings = []

    # Match based on listing type
    if listing_type == 'roommate':
        if not all([social_class, price_range, hobby, city]):
            flash("Please answer all questions before submitting the quiz.", "error")
            return redirect(url_for('quiz'))

        matched_listings = [
            listing for listing in roommate_listings
            if listing['social_class'] == social_class and
               listing['price_range'] == price_range and
               listing['hobby'] == hobby and
               listing['city'] == city
        ]

    elif listing_type == 'room':
        if not all([price_range, city]):
            flash("Please select price range and location for room listings.", "error")
            return redirect(url_for('quiz'))

        matched_listings = [
            listing for listing in rooms
            if listing['price_range'] == price_range and
               listing['city'] == city
        ]

    else:
        flash("Invalid listing type selected.", "error")
        return redirect(url_for('quiz'))

    # Render results page
    return render_template('result.html', result={
        "listing_type": listing_type,
        "social_class": social_class,
        "price_range": price_range,
        "hobby": hobby,
        "city": city,
        "listings": matched_listings
    })


if __name__ == '__main__':
    app.run(debug=True)@app.route('/')
def home():
    return render_template('index.html')

# Form to create a new listing
@app.route('/new-listing')
def new_listing():
    return render_template('new_listing.html')

# Redirect to quiz form
@app.route('/find-listing')
def find_listing():
    return redirect(url_for('quiz'))

# Quiz page: GET to display form, POST to process form
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'GET':
        return render_template('quiz.html')

    # Extract form data
    listing_type = request.form.get('listingType')
    social_class = request.form.get('socialClass')
    price_range = request.form.get('priceRange')
    hobby = request.form.get('hobby')
    city = request.form.get('city')

    # Validate listing type
    if not listing_type:
        flash("Please select a listing type.", "error")
        return redirect(url_for('quiz'))

    matched_listings = []

    # Match based on listing type
    if listing_type == 'roommate':
        if not all([social_class, price_range, hobby, city]):
            flash("Please answer all questions before submitting the quiz.", "error")
            return redirect(url_for('quiz'))

        matched_listings = [
            listing for listing in roommate_listings
            if listing['social_class'] == social_class and
               listing['price_range'] == price_range and
               listing['hobby'] == hobby and
               listing['city'] == city
        ] 

    elif listing_type == 'room':
        if not all([price_range, city]):
            flash("Please select price range and location for room listings.", "error")
            return redirect(url_for('quiz'))

        matched_listings = [
            listing for listing in rooms
            if listing['price_range'] == price_range and
               listing['city'] == city
        ]

    else:
        flash("Invalid listing type selected.", "error")
        return redirect(url_for('quiz'))

    # Render results page
    return render_template('result.html', result={
        "listing_type": listing_type,
        "social_class": social_class,
        "price_range": price_range,
        "hobby": hobby,
        "city": city,
        "listings": matched_listings
    })


if __name__ == '__main__':
    app.run(debug=True)