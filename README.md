# Knowledge-Graph-Construction-for-Food-Nutrition
The COVID-19 pandemic has prompted heightened attention to personal health, influencing various aspects of life. Studies suggest that a well-established dietary structure positively impacts both physiological and psychological well-being. Despite this, a disparity between nutritional science knowledge and public awareness impedes access to professional dietary guidance. This research seeks to bridge the gap by offering specialized nutritional advice to the general public through the integration of computer science knowledge.

Here's a simplified version of the research process diagram:
![process diagram](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/process%20diagram.png)
## 1.Data Collection:
Utilize "Nutrition Science," "Chinese Food Composition Table," Baidu Baike, and the Chinese Health and Wellness Website as data sources.

## 2.Data Processing:
Extract, process, and annotate data to build a corpus.  
Manually annotate chapters 2 to 11 of "Nutrition Science."Use regular expressions for rule-based extraction of content from the first three chapters of the "Chinese Food Composition Table," focusing on widely consumed and distributed food items.
 
## 3.Model Design:
Focus on nutrition, diseases, and demographics, constructing 7 node labels and 15 relationship types, with a designed pattern layer。

## 4.Data Fusion:
Address entity heterogeneity issues by designing an entity alignment algorithm based on the attribute of entities being resistant to change, using cosine similarity of word vectors to determine if they represent the same entity.

## 5.Data Storage:
Employ the Neo4j graph database to store nutritional data.    
Transform and import data into CSV format, utilizing Python's py2neo functions for entity and relationship creation.

## 6.Visualization and Recommendations:
Support basic queries and progressive retrieval.

Its pattern layer is as follows:
![pattern_lay](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/pattern%20layer.png)

![sample](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/semple.png)

![lab](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/lab.png)
