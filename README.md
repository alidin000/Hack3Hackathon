# Hack3Hackathon

<h2>Esportmanager.com</h2>
<h2>Leaderboard ELO System</h2>

<p>A hackathon project about creating ELO system for PUBG. Getting data from https://api.pubg.com</p>
<p>There are two parts of this project.</p>
<b><p>1. Leaderboard of players.</p></b>
<p> To make the ranking more accurate as a first step system counts each players performance percentage based on the mode that the user is playing with.</p>
<p>Game ranking on a classic mode will be counted with one algorithm and on arcade mode with another.</p>
<p>For instance, in classic mode since we have fixed time limit, focus stays on time interval player survived and number of killed enemies during that time. While in an arcade mode focus is on number of killed enemies - count of player’s deaths, because each time the player dies, he gives +1 kill number to the competitor.</p>
<p>Previously we described how player’s performance algorithm changes due to mode difference. As a second step we will talk about an algorithm that has to be used in both cases because it is not dependent from mode type, but it is important while searching for an ideal ranking system. If player uses sniper, SR then his ratio = headshots/bullet count, if the player plays with other weapons as SMG, AR the ratio is damage given/bullet count. </p>
<p>Also, to make the leaderboard better this ELO system will consider revive dead teammate count. All of this given counting algorithms will have appropriate percentage according to their priority and final algorithm will be algo.according to mode type * priority % + algo.according to players type * priority % + revive dead teammate * priority %.</p>
<p>As mentioned before to each game each user’s performance percentage will be analyzed and for every player only best 10 games will be stored and updated in a real time. To the leaderboard only average of those 10 games goes.</p>


# Technologies used
<ul>
  <li>Python</li>
  <li>MongoDB</li>
</ul>
