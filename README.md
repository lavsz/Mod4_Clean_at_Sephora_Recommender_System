# Sephora Clean Skincare - Recommender System
by Shenghao (Lavender) Zhang

## Overview
Natural and organic skincares have attracted a lot of attentions in the recent years. As one of the biggest Beauty Product retailers, Sephora launched their own category "Clean at Sephora" around June 2018. If you shop regularly there, you may find that products within this category usually has a green label on the product image. Based on Sephora's own statement, they listed about 50 differents that would set the bar for the "Clean" admission. Some common ingredients that quite often come across in the beauty world includes: 

- Paraben (a common preservative)
- Sulfates SLS (a common foaming agent)
- Phthalates (a common plasticizer/solvent/fixative)
- Mineral Oils 
- Triclosan (antibacterial agent)

With many people showing love for natural & organic products not only for personal health benefits and also for enjoying a more enviromentally friendly lifestyle, we can look at how to promote certain clean skincare products. 

## Some Overall Outlooks
Starting with looking at the skincare information, a few questions were posted and visualized. 

### 1. What are some commonly seen ingredients in the Clean Skincare?
![ingred](https://github.com/lavsz/Mod4_Project_Sephora/blob/main/Pictures/All_prod.png)

**Not bad! But this can be a little bit disappointing, right?** As we saw ingredients Phenoxyethanol and propanediol.

### 2. Does clinical test grants good results?

![clinc](https://github.com/lavsz/Mod4_Project_Sephora/blob/main/Pictures/Screen%20Shot%202021-01-13%20at%205.37.11%20PM.png)

### 3. Which category can be versatile while gets good ratings?

![ategory_rate](https://github.com/lavsz/Mod4_Project_Sephora/blob/main/Pictures/Screen%20Shot%202021-01-13%20at%205.39.27%20PM.png)

### 4. What can we see from our consumers?
![concerns](https://github.com/lavsz/Mod4_Project_Sephora/blob/main/Pictures/Screen%20Shot%202021-01-14%20at%205.55.02%20PM.png)


## Recommendation Systems

Three types of recommendation systems are being looked at:

### Collaborative Filtering System

A system that looks at the interactions between users and items, in our case, beauty shoppers and Clean skincare products. Who bought what products were used to determine users potential of purchasing a product that they have never bought in the past.

### Content-based System

A content-based system looks at the similarites of the items, in our case, the similarites of skincare products. If someone bought product A, a similar product B would be on the top recommendation list for this person. 

### Hybrid System

A hybrid system looks at both similarties of items as well as user-item interactions. In our case, the hybrid system added in both user-similarities as well item similarities on top of the user-item interactions to predict. 

### Results

It seems that a collaborative filtering system works the best so far with an accuracy score of 87%. In the Hybrid system, the system with user-similarity added in works the best. 

## Reference and librarys:
Surprise: documentation is [here](https://surprise.readthedocs.io/en/stable/getting_started.html)

LightFM: documentation is [here](https://making.lyst.com/lightfm/docs/home.html)

Clean at Sephora: product page is [here](https://www.sephora.com/beauty/clean-beauty-products)



