# Knowledge-Graph-Construction-for-Food-Nutrition
The COVID-19 pandemic has prompted heightened attention to personal health, influencing various aspects of life. Studies suggest that a well-established dietary structure positively impacts both physiological and psychological well-being. Despite this, a disparity between nutritional science knowledge and public awareness impedes access to professional dietary guidance. This research seeks to bridge the gap by offering specialized nutritional advice to the general public through the integration of computer science knowledge.

Here's a simplified version of the research process diagram:
![process diagram](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/process%20diagram.png)
## 1.Data Collection:
Utilize "Nutrition Science," "Chinese Food Composition Table," Baidu Baike, and the Chinese Health and Wellness Website as data sources.

## 2.Data Processing:
Extract, process, and annotate data to build a corpus.
Manually annotate chapters 2 to 11 of "Nutrition Science."
Use regular expressions for rule-based extraction of content from the first three chapters of the "Chinese Food Composition Table," focusing on widely consumed and distributed food items.
 
## 3.ModelDesign:
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
Taking the "cardiovascular disease" node as an example, the query results through the command: "MATCH (a:disease{name:"cardiovascular disease")-[r]->(b) RETURN a,b" are as shown in the figure. Through the query, it can be found that nutrients such as "coenzyme q10", "oleic acid" and "arginine" are beneficial to "cardiovascular diseases". Foods such as "spinach" and "cauliflower" are rich in these nutrients and are also good for "cardiovascular diseases", while foods such as "cream", "egg yolk" and "pork" are not good for "cardiovascular diseases". And the special group of "elderly people" are prone to such diseases and should pay attention to a healthy diet.
![sample](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/semple.png)
Due to the unpublished paper and the confidentiality of the project, we have only published a part of the data as a formal presentation. We have not yet published complete data in the dataset. The complete dataset and the construction method will be fully disclosed after the publication of the paper.
This team is from the Data Science and Knowledge Engineering Laboratory of Zhengzhou University of Light Industry.
![lab](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/lab.png)
