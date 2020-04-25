var n = 0; // noise input
var bg; // background
var tree;
var leafs = [];
var minHue, maxHue;


function setup() {
  var canvas = createCanvas(innerWidth -20, innerHeight -7);
  canvas.parent("plumbox");

  colorMode(HSB,360);
  noLoop();
  noStroke();
  
  createBackground();
  
  tree = createGraphics(width, height);  
  tree.parent("plumbox");
}

function draw() {     
  image(bg, 0, 0); // display background  
  createTree();
  setHue();
  // drawLeafs(10, 250, 0, 1);  // big smooth leafs
  drawLeafs(10, 300, 0, 1);  // big smooth leafs
  image(tree, 0, 0);  //display tree    
  drawLeafs(0, 20, 10, 40);  // small rigid leafs
  ground();  
}

// function mousePressed() {
 
//   redraw();
 
//   //delete leafs
//   for (var i = leafs.length; i >= 0; i--) {
//     leafs.pop();
//   }
  
// }

function createBackground() {
  bg = createGraphics(width, height);
  bg.parent("plumbox");
  bg.noStroke();
  for (var diam = 1.5*width; diam > 0.5*width; diam -= 20) {
    bg.noFill();
    bg.rect(width/2, height/2, diam, diam);
  }
}

function setHue() {
  var rdn0 = random(255);
  var rdn1 = random(255);
  minHue = min(rdn0, rdn1);
  maxHue = max(rdn0, rdn1);
}

function createTree() {
  tree.noStroke();
  tree.background(0, 0);  // clear PGraphics
  for (var i = 0; i < 3; i++) {
    tree.fill(map(i, 0, 2, 60, 20));
    branch(width/2, height, 70, -HALF_PI, 150, 0);
  }
}


function branch(x, y, bSize, theta, bLength, pos) {
  n += 0.01;  // increment noise input
  var diam = lerp(bSize, 0.7*bSize, pos/bLength);  // gradually reduce the diameter
  diam *= map(noise(n), 0, 1, 0.4, 1.6);  // multiply by noise to add variation
  
  tree.ellipse(x, y, diam, diam);
  if (bSize > 0.6) {
    if (pos < bLength) {
      x += cos(theta + random(-PI/10, PI/10));
      y += sin(theta + random(-PI/10, PI/10));
      branch(x, y, bSize, theta, bLength, pos+1);
    } else {
      leafs.push(new createVector(x, y));  // add a leaf at the varersection

      var drawleftBranch = random(1) > 0.1;
      var drawrightBranch = random(1) > 0.1;

      if (drawleftBranch) branch(x, y, random(0.5, 0.7)*bSize, theta - random(PI/15, PI/5), random(0.6, 0.8)*bLength, 0);
      if (drawrightBranch) branch(x, y, random(0.5, 0.7)*bSize, theta + random(PI/15, PI/5), random(0.6, 0.8)*bLength, 0);
      
      if (!drawleftBranch && !drawrightBranch) {  // if none of the branchs are drawn, draw a tip
        tree.push();
        tree.translate(x, y);
        tree.rotate(theta);
        tree.quad(0, -diam/2, 2*diam, -diam/6, 2*diam, diam/6, 0, diam/2);
        tree.pop();
      }
    }
  }
}

function drawLeafs(minDiam, maxDiam, minAlpha, maxAlpha) {
  for (var i = 0; i <leafs.length; i++) {
    var h = map(i, 0, leafs.length, minHue, maxHue);
    var s = 255;
    var b = 255;
    var a = random(minAlpha, maxAlpha);
    fill(h, s, b, a);
    var diam = random(minDiam, maxDiam);
    var jitterX = random(-30, 30);
    var jitterY = random(-30, 30);
    ellipse(leafs[i].x + jitterX,  leafs[i].y + jitterY, diam, diam);
  }
}

function ground() {
  fill(20);
  beginShape();
  vertex(0, height);
  for (var i = 0; i <= width; i += 50) {
    vertex(i, map(noise(n), 0, 1, height - 30, height));
    n += 0.1;
  }
  vertex(width, height);
  endShape();
}