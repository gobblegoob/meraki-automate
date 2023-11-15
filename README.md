<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** gobblegoob, meraki-automate, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Meraki-Automate</h3>

  <p align="center">
    Do you have a large number of Meraki MX or Z3 Teleworkor Gateways to deploy? Use this to rapidly deploy templated Z3 Teleworker Gateways or MX appliances 
  </p>
  <p align="left">
    <b>This script:</b> <br />
    1. Provisions networks <br />
    2. Adds security appliance to networks <br />
    3. Names security appliance <br />
    4. Applies a configuration template<br />
  </p>
    <a href="[contributors-url]https://github.com/gobblegoob/meraki-automate"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/gobblegoob/meraki-automate">View Demo</a>
    ·
    <a href="https://github.com/gobblegoob/meraki-automate/issues">Report Bug</a>
    ·
    <a href="https://github.com/gobblegoob/meraki-automate/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

### Built With

* meraki
* pandas



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
I sharp mind and a stout heart

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/gobblegoob/meraki-automate.git
   ```
2. Install requirements
   ```sh
   pip -r requirements.txt
   ```



<!-- USAGE EXAMPLES -->
## Usage

You will be required to add add the following informatiton to meraki.json
 * Meraki API Key
 * Organization Name
 * Source File, devicelist.csv by default
 
You will have to fill out the devicelist.csv which will require at least a Serial Number and device template as configured in the Meraki Portal.

You may then run the program 
```sh
python3 z3RapidDeploy.py
```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/gobblegoob/meraki-automate/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

<!-- Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email -->

Project Link: [https://github.com/gobblegoob/meraki-automate](https://github.com/gobblegoob/meraki-automate)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/gobblegoob/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/gobblegoob/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/gobblegoob/repo.svg?style=for-the-badge
[forks-url]: https://github.com/gobblegoob/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/gobblegoob/repo.svg?style=for-the-badge
[stars-url]: https://github.com/gobblegoob/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/gobblegoob/repo.svg?style=for-the-badge
[issues-url]: https://github.com/gobblegoob/repo/issues
[license-shield]: https://img.shields.io/github/license/gobblegoob/repo.svg?style=for-the-badge
[license-url]: https://github.com/gobblegoob/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gobblegoob
