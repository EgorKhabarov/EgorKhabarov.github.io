[chrome://dino/](chrome://dino/)

```javascript
Runner.instance_.setSpeed(1000)
```
```javascript
Runner.prototype.gameOver = function(){}
```

Setting the current score
Let’s set the score to 12345. You can set any other score less than 99999. The current score is reset on game over.
```javascript
Runner.instance_.distanceRan = 12345 / Runner.instance_.distanceMeter.config.COEFFICIENT
```

You can control how high the dino jumps by using the below function. Adjust the value as necessary.
```javascript
Runner.instance_.tRex.setJumpVelocity(10)
```

```javascript
Runner.prototype.gameOver = function(){}
Runner.instance_.setSpeed(1000)
```
