<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="https://github.com/AnishDubey27/Sky-Guardian/blob/main/media/weather.gif" border="0"></
  </p>
     

  <h1 align="center">Sky-Guardian</h1>

  <p align="center">
    An awesome Weather detection tool!
    <br />
    <a href="https://github.com/AnishDubey27/Sky-Guardian"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AnishDubey27/Sky-Guardian">View Demo</a>
    ·
    <a href="https://github.com/AnishDubey27/Sky-Guardian/issues">Report Bug</a>
    ·
    <a href="https://github.com/AnishDubey27/Sky-Guardian/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project


This is a weather app as it name suggests. I started this project in order to test my command over python and overcome the challenges which come along the way while building this project from scratch.

I recently added a dockerfile to the project to increase the scalability of the application and will be using other DevOps based tools in the future.

Use the `README.md` to get started.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built with

<p align="center">
  <a href="https://www.djangoproject.com/">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQD8EHO5qiBw-SQtVfaoJeyQqFQFlO39xzrOdnLaZw4Sw&s" alt="Django" width="130" height="70">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/1200px-HTML5_logo_and_wordmark.svg.png" alt="HTML" width="100">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/1200px-CSS3_logo_and_wordmark.svg.png" alt="CSS" width="100">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png" alt="JavaScript" width="100">
  </a>
  <a href="https://en.wikipedia.org/wiki/SQL">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/1200px-Postgresql_elephant.svg.png" alt="SQL" width="100">
  </a>
  <a href="https://www.python.org/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" alt="Python" width="100">
  </a>
  <a href="https://www.docker.com/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Docker_%28container_engine%29_logo.svg/1200px-Docker_%28container_engine%29_logo.svg.png" alt="Docker" width="150" height="70">
  </a>
  <a href="https://www.jenkins.io/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Jenkins_logo.svg/339px-Jenkins_logo.svg.png?20120629215426" alt="Jenkins" width="100">
</p>



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* django
  ```sh
  pip install django
  ```

### Installation

Follow the steps below to install the application

1. Clone the repo
   ```sh
   git clone https://github.com/AnishDubey27/Sky-Guardian.git
   ```
2. Go inside the newly created directory
   ```sh
   cd Sky-Guardian
   ```
3. Run the project locally
   ```sh
   python manage.py runserver
   ```

Alternatively, using docker:
1. Clone the repo
   ```sh
   git clone https://github.com/AnishDubey27/Sky-Guardian.git
   ```
2. Go inside the newly created directory
   ```sh
   cd Sky-Guardian
   ```
3. Run the project
   ```sh
   docker-compose up
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing
- Take a look at the existing [Issues](https://github.com/AnishDubey27/Sky-Guardian/issues) 
- Fork the Repo create a branch for any issue that you are working on and commit your work.
- Create a ** [Pull Request](https://github.com/AnishDubey27/Sky-Guardian/pulls), which will be promptly reviewed and given suggestions for improvements by the community.
- Add screenshots or screen captures to your Pull Request to help us understand the effects of the changes that are included in your commits.

## How to make a Pull Request?

**1.** Start by forking the [**Sky-Guardian**](https://github.com/AnishDubey27/Sky-Guardian) repository. Click on the <a href="https://github.com/AnishDubey27/Sky-Guardian/fork"><img src="https://i.imgur.com/G4z1kEe.png" height="21" width="21"></a> symbol at the top right corner.

**2.** Clone your forked repository:

```bash
git clone https://github.com/<your-github-username>/Sky-Guardian.git
```

**3.** Navigate to the new project directory:

```bash
cd Sky-Guardian
```

**4.** Set upstream command:

```bash
git remote add upstream https://github.com/AnishDubey27/Sky-Guardian.git
```

**5.** Create a new branch:

```bash
git checkout -b YourBranchName
```
<i>or</i>
```bash
git branch YourBranchName
git switch YourBranchName
``` 

**6.** Sync your fork or local repository with the origin repository:

- In your forked repository click on "Fetch upstream"
- Click "Fetch and merge".

### Alternatively, Git CLI way to Sync forked repository with origin repository:

```bash
git fetch upstream
```

```bash
git merge upstream/main
```

### [Github Docs](https://docs.github.com/en/github/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github) for Syncing

**7.** Make your changes to the source code.

**8.** Stage your changes and commit:

⚠️ **Make sure** not to commit `package.json` or `package-lock.json` file

⚠️ **Make sure** not to run the commands ```git add .``` or ```git add *```. Instead, stage your changes for each file/folder

```bash
git add file/folder
```

```bash
git commit -m "<your_commit_message>"
```

**9.** Push your local commits to the remote repository:

```bash
git push origin YourBranchName
```

**10.** Create a [Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)!

**11.** **Congratulations!** You've made your first contribution! 🙌🏼

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Anish Dubey - [@Anish_Dubey_](https://twitter.com/Anish_Dubey_) - anishdubey100@gmail.com

Project Link: [https://github.com/AnishDubey27/Sky-Guardian](https://github.com/AnishDubey27/Sky-Guardian)

<p align="right">(<a href="#readme-top">back to top</a>)</p>








<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AnishDubey27/Sky-Guardian.svg?style=for-the-badge
[contributors-url]: https://github.com/AnishDubey27/Sky-Guardian/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AnishDubey27/Sky-Guardian.svg?style=for-the-badge
[forks-url]: https://github.com/AnishDubey27/Sky-Guardian/network/members
[stars-shield]: https://img.shields.io/github/stars/AnishDubey27/Sky-Guardian.svg?style=for-the-badge
[stars-url]: https://github.com/AnishDubey27/Sky-Guardian/stargazers
[issues-shield]: https://img.shields.io/github/issues/AnishDubey27/Sky-Guardian.svg?style=for-the-badge
[issues-url]: https://github.com/AnishDubey27/Sky-Guardian/issues
[license-shield]: https://img.shields.io/github/license/AnishDubey27/Sky-Guardian.svg?style=for-the-badge
[license-url]: https://github.com/AnishDubey27/Sky-Guardian/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/anish-dubey

[product-screenshot]: images/screenshot.png
[Django]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
=======
<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="https://github.com/AnishDubey27/Sky-Guardian/blob/main/media/weather.gif" border="0"></
  </p>
     
<h1 align="center">Sky-Guardian</h1>
  <p align="center">
    An awesome Weather detection tool!
    <br />
    <a href="https://github.com/AnishDubey27/Sky-Guardian"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AnishDubey27/Sky-Guardian">View Demo</a>
    ·
    <a href="https://github.com/AnishDubey27/Sky-Guardian/issues">Report Bug</a>
    ·
    <a href="https://github.com/AnishDubey27/Sky-Guardian/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project


This is a weather app as it name suggests. I started this project in order to test my command over python and overcome the challenges which come along the way while building this project from scratch.

I recently added a dockerfile to the project to increase the scalability of the application and will be using other DevOps based tools in the future.

Use the `README.md` to get started.


<p align="right">(<a href="#readme-top">back to top</a>)</p>
### Built With


<p align="center">
  <a href="https://www.djangoproject.com/">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQD8EHO5qiBw-SQtVfaoJeyQqFQFlO39xzrOdnLaZw4Sw&s" alt="Django" width="130" height="70">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/1200px-HTML5_logo_and_wordmark.svg.png" alt="HTML" width="100">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/1200px-CSS3_logo_and_wordmark.svg.png" alt="CSS" width="100">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png" alt="JavaScript" width="100">
  </a>
  <a href="https://en.wikipedia.org/wiki/SQL">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/1200px-Postgresql_elephant.svg.png" alt="SQL" width="100">
  </a>
  <a href="https://www.python.org/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" alt="Python" width="100">
  </a>
  <a href="https://www.docker.com/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Docker_%28container_engine%29_logo.svg/1200px-Docker_%28container_engine%29_logo.svg.png" alt="Docker" width="150" height="70">
  </a>
  <a href="https://www.jenkins.io/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Jenkins_logo.svg/339px-Jenkins_logo.svg.png?20120629215426" alt="Jenkins" width="100">
</p>



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* django
  ```sh
  pip install django
  ```

### Installation

Follow the steps below to install the application

1. Clone the repo
   ```sh
   git clone https://github.com/AnishDubey27/Sky-Guardian.git
   ```
2. Go inside the newly created directory
   ```sh
   cd Sky-Guardian
   ```
3. Run the project locally
   ```sh
   python manage.py runserver
   ```

Alternatively, using docker:
1. Clone the repo
   ```sh
   git clone https://github.com/AnishDubey27/Sky-Guardian.git
   ```
2. Go inside the newly created directory
   ```sh
   cd Sky-Guardian
   ```
3. Run the project
   ```sh
   docker-compose up
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing
- Take a look at the existing [Issues](https://github.com/AnishDubey27/Sky-Guardian/issues) 
- Fork the Repo create a branch for any issue that you are working on and commit your work.
- Create a ** [Pull Request](https://github.com/AnishDubey27/Sky-Guardian/pulls), which will be promptly reviewed and given suggestions for improvements by the community.
- Add screenshots or screen captures to your Pull Request to help us understand the effects of the changes that are included in your commits.

## How to make a Pull Request?

**1.** Start by forking the [**Sky-Guardian**](https://github.com/AnishDubey27/Sky-Guardian) repository. Click on the <a href="https://github.com/AnishDubey27/Sky-Guardian/fork"><img src="https://i.imgur.com/G4z1kEe.png" height="21" width="21"></a> symbol at the top right corner.

**2.** Clone your forked repository:

```bash
git clone https://github.com/<your-github-username>/Sky-Guardian.git
```

**3.** Navigate to the new project directory:

```bash
cd Sky-Guardian
```

**4.** Set upstream command:

```bash
git remote add upstream https://github.com/AnishDubey27/Sky-Guardian.git
```

**5.** Create a new branch:

```bash
git checkout -b YourBranchName
```
<i>or</i>
```bash
git branch YourBranchName
git switch YourBranchName
``` 

**6.** Sync your fork or local repository with the origin repository:

- In your forked repository click on "Fetch upstream"
- Click "Fetch and merge".

### Alternatively, Git CLI way to Sync forked repository with origin repository:

```bash
git fetch upstream
```

```bash
git merge upstream/main
```

### [Github Docs](https://docs.github.com/en/github/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github) for Syncing

**7.** Make your changes to the source code.

**8.** Stage your changes and commit:

⚠️ **Make sure** not to commit `package.json` or `package-lock.json` file

⚠️ **Make sure** not to run the commands ```git add .``` or ```git add *```. Instead, stage your changes for each file/folder

```bash
git add file/folder
```

```bash
git commit -m "<your_commit_message>"
```

**9.** Push your local commits to the remote repository:

```bash
git push origin YourBranchName
```

**10.** Create a [Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)!

**11.** **Congratulations!** You've made your first contribution! 🙌🏼

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Anish Dubey - [@Anish_Dubey_](https://twitter.com/Anish_Dubey_) - anishdubey100@gmail.com

Project Link: [https://github.com/AnishDubey27/Sky-Guardian](https://github.com/AnishDubey27/Sky-Guardian)

<p align="right">(<a href="#readme-top">back to top</a>)</p>








<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AnishDubey27/Sky-Guardian.svg?style=for-the-badge
[contributors-url]: https://github.com/AnishDubey27/Sky-Guardian/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AnishDubey27/Sky-Guardian.svg?style=for-the-badge
[forks-url]: https://github.com/AnishDubey27/Sky-Guardian/network/members
[stars-shield]: https://img.shields.io/github/stars/AnishDubey27/Sky-Guardian.svg?style=for-the-badge
[stars-url]: https://github.com/AnishDubey27/Sky-Guardian/stargazers
[issues-shield]: https://img.shields.io/github/issues/AnishDubey27/Sky-Guardian.svg?style=for-the-badge
[issues-url]: https://github.com/AnishDubey27/Sky-Guardian/issues
[license-shield]: https://img.shields.io/github/license/AnishDubey27/Sky-Guardian.svg?style=for-the-badge
[license-url]: https://github.com/AnishDubey27/Sky-Guardian/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/anish-dubey

[product-screenshot]: images/screenshot.png
[Django]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
>>>>>>> ae59e2ada3f8e6a7251b7a8e7d9d7a7bfed20b53
