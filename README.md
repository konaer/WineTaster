
<h3 align="center">Wine Quality Prediction Tool</h3>

  <p align="center">
    This is a machine learning prediction tool basd on Spark over AWS.
    <br />
    <a href="https://github.com/konaer/WineQualityPrediction/"><strong>Explore the source code »</strong></a>
    <br />
    <br />
    <a href="https://github.com/konaer/WineQualityPrediction/issues">Report Bug</a>
  </p>


## About the project

This is a wine quality prediction ML model in Spark over AWS. The model is trained in parallel on multiple EC2 instances. Then the model is saved and loaded in an application that will perform wine quality prediction. The whole application is easy to deploy by a docker image built for users (please see <a href="https://github.com/konaer/WineQualityPrediction/blob/main/UserGuidance.pdf">user guide</a> for more info). The accuracy is 84.6% in average.   


## Tech Stack of the project

* Develop parallel machine learning (ML) applications in **Amazon AWS** cloud platform
* Use **Apache Spark** to train an ML model in parallel on multiple **EC2** instances
* Use **Spark’s MLlib** to use an ML model in the cloud
* Use **Docker** to create a container for ML model to simplify model deployment
* Use **Python** as coding lenguage
* Use **Linux** as operation system


## Deploy and use
Please check <a href="https://github.com/konaer/WineQualityPrediction/blob/main/UserGuidance.pdf">user guidance</a> here.


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Edward Kong - [@LinkedIn](https://www.linkedin.com/in/edwardkong123/) - edkong831@gmail.com
