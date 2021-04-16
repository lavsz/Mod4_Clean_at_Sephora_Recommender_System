# Sephora Clean Skincare - Recommender System
by Shenghao (Lavender) Zhang

## Overview
Natural and organic skincares have attracted a lot of attentions in the recent years. As one of the biggest Beauty Product retailers, Sephora launched their own category "Clean at Sephora" around June 2018. If you shop regularly there, you may find that products within this category usually has a green label on the product image. Based on Sephora's own statement, they listed about 50 differents that would set the bar for the "Clean" admission. Some common ingredients that quite often come across in the beauty world includes: 

- Paraben (a common preservative)
- Sulfates SLS (a common foaming agent)
- Phthalates (a common plasticizer/solvent/fixative)
- Mineral Oils 
- Triclosan (antibacterial agent)

With many people showing love for natural & organic products not only for personal health benefits and also for enjoying a more enviromentally friendly lifestyle, we can look at how to promote certain clean skincare products most efficiently through different recommender systems. 

## Some Overall Outlooks
Starting with looking at the skincare information, a few questions were posted and visualized. 

### 1. What are some commonly seen ingredients in the Clean Skincare?
<img src = 'https://github.com/lavsz/Mod4_Project_Sephora/blob/main/Pictures/All_prod.png' width="450" height="450">

Note: **Not bad! But this can be a little bit disappointing, right?** As we saw controversial ingredients Phenoxyethanol and Sodium Benzoate.

### 2. Does clinical test grants good results?

<img src = 'https://github.com/lavsz/Mod4_Project_Sephora/blob/main/Pictures/Screen%20Shot%202021-01-13%20at%205.37.11%20PM.png' width="500" height="300">

Note: overall, clinically-tested products tend to achieve slightly better ratings than those that were not, particularlly in face moisturizer and face serums.

### 3. Which category can be versatile while gets good ratings?

<img src = 'https://github.com/lavsz/Mod4_Project_Sephora/blob/main/Pictures/Screen%20Shot%202021-01-13%20at%205.39.27%20PM.png' width="600" height="300">

Note: Face mask is a category that can be versatile and with relative high ratings. 

## Recommendation Systems

To better differentiate user's review on products, the product that was rated 1 or 2 by a user was then converted to 0 (not likely to buy and satify) and rating above 3 are converted to 1 (likely to buy and like).

Two types of recommendation systems are being looked at:

### Collaborative Filtering System

A system that looks at the interactions between users and items, in our case, beauty shoppers and Clean skincare products. Who bought what products were used to determine users potential of purchasing a product that they have never bought in the past. The package Surprise was used to build this system with evaluations of many different algorithms including but not limited to SVD and Normal Predictor etc. The highest accuracy score was 88% through the SVD algorithm. 


### Hybrid System

A hybrid system looks at both similarties of items as well as user-item interactions. In our case, the hybrid system added in both user-similarities as well item similarities on top of the user-item interactions to predict. The package LightFM was used to build this system. Different types of contents were evaluated including user features (skin type, skin concerns, reviews on product etc.) and product features (brand, ingredients, product type etc.). Due to LightFM's limitation, the Hybrid system could not be evaluated on the accuracy score. The best hybrid system was able to achieve 87% on the average auc score. 

### Results

By evaluating all the recommendation system, the collaborative filtering system works well with high accuracy score. Many times, in the case of choosing a product, users tend to look at how many people had purchased a specific item and how many gave positive feedbacks. 

In the Hybrid system, the system with user-features added in has higher auc score than the system with item-features or both user and item features. This result demonstrates that similarity among users can be more important than similarity among products when promoting a product, as consumers tend to believe more in real life comments and experiences more than what product marketing contents.

## Further Improvement:

LightFM is a relatively new recommendation system builder. With its capacity of incorporting features from both consumers and products, it would be great to research more on larger dataset to improve the recommendation system for all beauty products.  

Beauty product purchase also would be largely affected by geographical location as climate plays a role in skin concerns. Information about user's location can be very helpful in providing insights for customized promotion in different regions. 

## Major Libraries Used:
Webscrapping & Acquisition:
- Selenium
- Requests

Recommender System Modeling:
- LightFM
- Surprise

## Reference:
Surprise: documentation is [here](https://surprise.readthedocs.io/en/stable/getting_started.html)

LightFM: documentation is [here](https://making.lyst.com/lightfm/docs/home.html)

Clean at Sephora: product page is [here](https://www.sephora.com/beauty/clean-beauty-products)



