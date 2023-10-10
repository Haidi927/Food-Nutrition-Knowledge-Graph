# Knowledge-Graph-Construction-for-Food-Nutrition

Research Significance:
The COVID-19 pandemic has significantly altered various aspects of life, leading to an increased emphasis on personal health. Studies indicate that a sound dietary structure is conducive to both physiological and psychological well-being. However, a gap exists between nutritional science knowledge and the general public, hindering access to professional dietary advice.
This research aims to provide specialized nutritional guidance to the general public through the application of computer science knowledge.
The project follows the outlined procedure:

Data Collection:
This study utilizes data from "Nutrition Science," the "Chinese Food Composition Table," Baidu Baike, and the Chinese Health and Wellness Website.
Data Processing:
After extracting, processing, and annotating data from the mentioned sources, a preliminary corpus dataset is established. Specifically, chapters 2 to 11 of "Nutrition Science" are manually annotated. Additionally, a rule-based approach, utilizing regular expressions, is employed to extract content from the first three chapters of the "Chinese Food Composition Table," focusing on widely consumed and distributed food items.
Model Design:
This research focuses on nutrition, diseases, and demographics, constructing 7 node labels and 15 relationship types, with a designed pattern layer.
Data Fusion:
The dataset presents entity heterogeneity issues, wherein entities with different names point to the same entity. This study addresses this by designing an entity alignment algorithm based on the attribute of entities being resistant to change, using cosine similarity of word vectors to determine if they represent the same entity.
Data Storage:
Neo4j graph database is employed to store nutritional data. Extracted data is transformed into CSV format, and the py2neo functions in Python are utilized for entity and relationship creation, facilitated by the merger function for data import.
Visualization and Recommendations:
This research supports basic queries and progressive retrieval.
Its pattern layer is as follows:
![pattern_lay](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/pattern%20layer.png)
Taking the "cardiovascular disease" node as an example, the query results through the command: "MATCH (a:disease{name:"cardiovascular disease")-[r]->(b) RETURN a,b" are as shown in the figure. Through the query, it can be found that nutrients such as "coenzyme q10", "oleic acid" and "arginine" are beneficial to "cardiovascular diseases". Foods such as "spinach" and "cauliflower" are rich in these nutrients and are also good for "cardiovascular diseases", while foods such as "cream", "egg yolk" and "pork" are not good for "cardiovascular diseases". And the special group of "elderly people" are prone to such diseases and should pay attention to a healthy diet.
![sample](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/semple.png)
Due to the unpublished paper and the confidentiality of the project, we have only published a part of the data as a formal presentation. We have not yet published complete data in the dataset. The complete dataset and the construction method will be fully disclosed after the publication of the paper.
This team is from the Data Science and Knowledge Engineering Laboratory of Zhengzhou University of Light Industry.
![lab](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/lab.png)
