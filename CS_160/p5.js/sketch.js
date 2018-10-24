function setup() {
  createCanvas(1000, 1000);
  // put setup code here
}

function draw() {
  line(240, 300, 240, 568);
  line(240,568,320,568)
  
  if (mouseIsPressed) {
    fill(0);
    } else {
    fill(255);
    }
    rect(mouseX, mouseY, 30, 30);
    strokeWeight(4);
  // put drawing code here
}