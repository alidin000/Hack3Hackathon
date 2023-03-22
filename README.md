# Hack3Hackathon Challenge

<h2>Esportmanager.com</h2>
<h2>Leaderboard ELO System</h2>

<p>A hackathon project about creating ELO system for PUBG. Getting data from https://api.pubg.com</p>
<p>There are two parts of this project.</p>
<b><h2>1. Leaderboard of players.</h2></b>
<p> To make the ranking more accurate as a first step system counts each players performance percentage based on the mode that the user is playing with.</p>
<p>Game ranking on a classic mode will be counted with one algorithm and on arcade mode with another.</p>
<p>For instance, in classic mode since we have fixed time limit, focus stays on time interval player survived and number of killed enemies during that time. While in an arcade mode focus is on number of killed enemies - count of player’s deaths, because each time the player dies, he gives +1 kill number to the competitor.</p>
<p>Previously we described how player’s performance algorithm changes due to mode difference. As a second step we will talk about an algorithm that has to be used in both cases because it is not dependent from mode type, but it is important while searching for an ideal ranking system. If player uses sniper, SR then his ratio = headshots/bullet count, if the player plays with other weapons as SMG, AR the ratio is damage given/bullet count. </p>
<p>Also, to make the leaderboard better this ELO system will consider revive dead teammate count. All of this given counting algorithms will have appropriate percentage according to their priority and final algorithm will be algo.according to mode type * priority % + algo.according to players type * priority % + revive dead teammate * priority %.</p>
<p>As mentioned before to each game each user’s performance percentage will be analyzed and for every player only best 10 games will be stored and updated in a real time. To the leaderboard only average of those 10 games goes.</p>
<b><h2>2. Teammate, enemy match finder.</h2></b>
<p>In this part of the challenge, we will use the same ranking from leaderboard in order to find teammates, enemies with approximately equal rankings.</p>
<p>Top players will play with top once’s in the leaderboard. Team arrangement will be based on current player’s level of experience. If player is experienced his team will be formed from experienced teammates.</p>
<p>In team formation players age, language and location will also be considered so that they can understand each other and communicate better.</p>
<p>Also, in order to form the best team in classic mode there must be 1 doctor, 1 close combat and 2 snipers. And in arcade mode team needs 1 doctor, 1 sniper and 2 close combats approximately. For example, if current user is a sniper, then the system searches for other teammates from the ranking excluding the current player. After team is formed teams average strength is counted according to each members performance ratio and from all given team choices most suitable team will be offered.</p>


# Technologies used
<ul>
  <li>Python</li>
  <li>MongoDB</li>
</ul>
