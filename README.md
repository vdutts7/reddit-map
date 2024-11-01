# Mapping Reddit comments




<div align="center">


  <img src="public/btc.png" alt="Bitcoin Logo" width="80" height="80" />
  <img src="public/node-js.png" alt="Node.js Logo" width="" height="67"/>

  <h1 align="center">
        Visual Map | Reddit comments
    </h1>
    <p align="center"> 
        <i><b>Visualizing maps of Reddit comments based on semantic similarity</b></i>
        <br /> 
    </p>

[![Github][github]][github-url]


</div>



## Table of Contents

  <ol>
    <a href="#FREE-200-USD-cloud-credits">💸 FREE 200 USD cloud credits</a><br/>
    <a href="#about">📝 About</a><br/>
    <a href="#how-to-build">💻 How to build</a><br/>
    <a href="#tools-used">🔧 Tools used</a>
        <ul>
        </ul>
    <a href="#contact">👤 Contact</a>
  </ol>

<br/>

## 💸FREE 200 USD cloud credits

Click the banner to activate $200 free personal cloud credits on DigitalOcean (deploy anything).

<div style="display: flex; align-items: center; justify-content: center; width: 400px;"> 
    <a href="https://www.digitalocean.com/?refcode=2aa0ec7cfd0e&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge">
        <img src="https://res.cloudinary.com/dnz16usmk/image/upload/v1709301461/digitalocean-referral.png"
            width="150"
        />
    </a>
</div>



## 📝About
- how to automate the extraction, processing, and mapping of Reddit comments using Python and Nomic Atlas
- use the Reddit API to fetch comments from a Reddit post URL
- store the data in Nomic Atlas
- create an Atlas map on the dataset to produce a visualization


## 💻How to build


### Setup:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Environemnt variables

Get your Reddit developer credentials: https://www.reddit.com/prefs/apps 
```
REDDIT_CLIENT_ID=<your_client_id>
REDDIT_CLIENT_SECRET=<your_client_secret>
REDDIT_USER_AGENT=<your_user_agent>
```

Run the script:
```
python reddit.py
```


Example:
```
(venv) (base) vdutts7@Vacbook-Vro reddit-map % python reddit.py             
Enter Reddit post URL: https://www.reddit.com/r/pics/comments/5bx4bx/thanks_obama/
Loading comments...
Found 5936 comments to process
Progress: 1.7% (100/5936 comments processed)
Progress: 3.4% (200/5936 comments processed)
Progress: 5.1% (300/5936 comments processed)
Progress: 6.7% (400/5936 comments processed)
Progress: 8.4% (500/5936 comments processed)
Progress: 10.1% (600/5936 comments processed)
Progress: 11.8% (700/5936 comments processed)
Progress: 13.5% (800/5936 comments processed)
Progress: 15.2% (900/5936 comments processed)
Progress: 16.8% (1000/5936 comments processed)
Progress: 18.5% (1100/5936 comments processed)
Progress: 20.2% (1200/5936 comments processed)
Progress: 21.9% (1300/5936 comments processed)
Progress: 23.6% (1400/5936 comments processed)
Progress: 25.3% (1500/5936 comments processed)
Progress: 27.0% (1600/5936 comments processed)
Progress: 28.6% (1700/5936 comments processed)
Progress: 30.3% (1800/5936 comments processed)
Progress: 32.0% (1900/5936 comments processed)
Progress: 33.7% (2000/5936 comments processed)
Progress: 35.4% (2100/5936 comments processed)
Progress: 37.1% (2200/5936 comments processed)
Progress: 38.7% (2300/5936 comments processed)
Progress: 40.4% (2400/5936 comments processed)
Progress: 42.1% (2500/5936 comments processed)
Progress: 43.8% (2600/5936 comments processed)
Progress: 45.5% (2700/5936 comments processed)
Progress: 47.2% (2800/5936 comments processed)
Progress: 48.9% (2900/5936 comments processed)
Progress: 50.5% (3000/5936 comments processed)
Progress: 52.2% (3100/5936 comments processed)
Progress: 53.9% (3200/5936 comments processed)
Progress: 55.6% (3300/5936 comments processed)
Progress: 57.3% (3400/5936 comments processed)
Progress: 59.0% (3500/5936 comments processed)
Progress: 60.6% (3600/5936 comments processed)
Progress: 62.3% (3700/5936 comments processed)
Progress: 64.0% (3800/5936 comments processed)
Progress: 65.7% (3900/5936 comments processed)
Progress: 67.4% (4000/5936 comments processed)
Progress: 69.1% (4100/5936 comments processed)
Progress: 70.8% (4200/5936 comments processed)
Progress: 72.4% (4300/5936 comments processed)
Progress: 74.1% (4400/5936 comments processed)
Progress: 75.8% (4500/5936 comments processed)
Progress: 77.5% (4600/5936 comments processed)
Progress: 79.2% (4700/5936 comments processed)
Progress: 80.9% (4800/5936 comments processed)
Progress: 82.5% (4900/5936 comments processed)
Progress: 84.2% (5000/5936 comments processed)
Progress: 85.9% (5100/5936 comments processed)
Progress: 87.6% (5200/5936 comments processed)
Progress: 89.3% (5300/5936 comments processed)
Progress: 91.0% (5400/5936 comments processed)
Progress: 92.7% (5500/5936 comments processed)
Progress: 94.3% (5600/5936 comments processed)
Progress: 96.0% (5700/5936 comments processed)
Progress: 97.7% (5800/5936 comments processed)
Progress: 99.4% (5900/5936 comments processed)
Completed! Total comments fetched: 5936
Comments saved to reddit_comments_1730443051.csv
```


## 🔧Tools Used

[![TypeScript][typescript]][typescript-url]
[![Node.js][nodejs]][nodejs-url]
[![Crypto][crypto]][crypto-url]

## 👤Contact

<!-- Replace placeholders with your actual contact information -->
[![Email][email]][email-url]
[![Twitter][twitter]][twitter-url]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[typescript]: https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white
[typescript-url]: https://www.typescriptlang.org/
[nodejs]: https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white
[nodejs-url]: https://nodejs.org/
[crypto]: https://img.shields.io/badge/Crypto-000000?style=for-the-badge&logo=node.js&logoColor=white
[crypto-url]: https://nodejs.org/api/crypto.html
[email]: https://img.shields.io/badge/me@vd7.io-FFCA28?style=for-the-badge&logo=Gmail&logoColor=00bbff&color=black
[email-url]: #
[github]: https://img.shields.io/badge/💻Github-000000?style=for-the-badge
[github-url]: https://github.com/vdutts7/blockchain-js
[twitter]: https://img.shields.io/badge/Twitter-FFCA28?style=for-the-badge&logo=Twitter&logoColor=00bbff&color=black
[twitter-url]: https://twitter.com/vdutts7/
