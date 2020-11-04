int Bx_pos=305;
int By_pos=255;
int Bspeed_x = 1;
int Bspeed_y = 0;
int Brect_w = 5;
int Brect_h = 5;
int radius = 5;
int x=400;
int y=250;
int w=10;
int h=70;

int hue1 = 0;
int hue2 = 1000;

void setup() {
  background(0,0,0);
  size(500,500);
  noStroke();
  //rectMode(CENTER);
}

void draw() {
  rect(250,250,40,40);
  fill(255, 0, 0);
  rect(400,250,10,70);
  fill(255, 255, 0);
  fill(0);
  //Conditionals for Rectangle B
  //in up right area, going into down right
  if ((Bx_pos >= width-Brect_w) && !(By_pos >= width-Brect_h)){
    Bspeed_x = Bspeed_x * -1;}
  //in down right area, going into down left
  if (!(Bx_pos >= width-Brect_w) && (By_pos >= width-Brect_h)) {
    Bspeed_y = Bspeed_y * -1;}
  //in down left, going into up left
  if ((Bx_pos <= 0) && !(By_pos >= width-Brect_h)) {
    Bspeed_x = Bspeed_x * -1;}
  //in up left, going into up right
  if (!(Bx_pos >= width-Brect_w) && (By_pos <= 0)) {
    Bspeed_y = Bspeed_y * -1;}
  
  
  //side to side collsion dimensions
  if ((Bx_pos > x - radius && Bx_pos < x + w + radius && By_pos > y && By_pos < y + h)||
      (Bx_pos > x && Bx_pos < x + w && By_pos > y - radius && By_pos < y + h + radius)) {
    fill(0, 255, 0);
    rect(Bx_pos+radius,By_pos,4,4);
    Bspeed_x = Bspeed_x * -0;
  }
  
    //side to side collsion dimensions
  if ((Bx_pos > 250 - radius && Bx_pos < 250 + 40 + radius && By_pos > y && By_pos < 250 + 40)||
      (Bx_pos > 250 && Bx_pos < 250 + 40 && By_pos > 250 - radius && By_pos < 250 +  + radius)) {
    fill(255, 0, 250);
    Bspeed_x = Bspeed_x * -1;
  }

  //top left corner
  if (dist(x, y, mouseX, mouseY) < radius) {
    fill(255, 0, 0);
  }
  //bottom right corner
  if (dist(x + w, y + h, mouseX, mouseY) < radius) {
    fill(0, 0, 255);
  }
  //top right corner
  if (dist(x + w, y, mouseX, mouseY) < radius) {
    fill(0, 255, 0);
  }
  //bottom left corner
  if (dist(x, y + h, mouseX, mouseY) < radius) {
    fill(255, 250, 0);
  }

  
  
  //colorMode(HSB);
  //ellipseMode(CORNER);
  
  //Rectangle B
  Bx_pos = Bx_pos + Bspeed_x;
  By_pos = By_pos + Bspeed_y;
  //fill (0,0,0,100);
  ellipse(Bx_pos,By_pos,Brect_w,Brect_h);
  
  

  colorMode(RGB);
  fill(255,230,255,10);
  rect(0,0,width,height);
}
