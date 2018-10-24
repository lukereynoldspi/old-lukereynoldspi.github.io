function setup() {
  createCanvas(2000, 1000);
  // put setup code here
}

function draw() {
 
  line(240, 300, 240, 568);
  line(240, 568, 320, 568);

  
  if (mouseIsPressed) {
    fill(199, 21, 133);
    line(0,0, mouseX,mouseY);
    stroke(199, 21, 133);
    strokeWeight(4);
    } else {
    line(2000,1000, mouseX,mouseY);
    stroke(0,0,0);
    strokeWeight(4);
    fill(255);
    }
    rect(mouseX, mouseY, 120, 10);
    strokeWeight(4);
    
  // put drawing code here
}