
var canvas = document.querySelector('canvas'); 
var c = canvas.getContext('2d'); 
var canvasContainer = document.getElementById("canvas-container")

canvas.style.position = "absolute";
canvas.style.top = 0;
canvas.style.left = 0;
canvas.style.margin = 0;
canvas.style.padding = 0;
canvas.width = document.body.offsetWidth;
canvas.height = document.body.offsetHeight; 




var mouse = {
    x: undefined, 
    y:undefined
}


//To add an event listener in JS we use the window.addEventListener function
//it takes an event and a callback which takes in an event argument as its parameters. 
window.addEventListener("mousemove", function (event) {
    mouse.x = event.x; 
    mouse.y = event.y; 
} )

window.addEventListener("resize", function (event) {

    canvas.width = window.innerWidth; 
    canvas.height = window.innerHeight; 
    var circleArr = init(); 
})

function Circle (x, y, radius, dx, dy, col) {
    this.x = x; 
    this.y = y; 
    this.dx = dx; 
    this.dy = dy; 
    this.radius = radius; 
    this.col = col; 
    this.minRad = radius; 
 

    this.draw = function () {

        c.beginPath(); 
        c.arc(this.x, this.y,this.radius, 0, Math.PI *2, false); 
        c.fillStyle = this.col; 
        c.fill(); 
    }
    this.update = function () {
        if (this.x + this.radius > window.innerWidth || this.x - this.radius < 0) this.dx = -this.dx; 
        if (this.y + this.radius > window.innerHeight || this.y - this.radius < 0) this.dy = -this.dy; 

        this.x += this.dx; 
        this.y += this.dy; 


        
        this.draw(); 
    }
    
}



var circleArr = []; 
function init() {
    circleArr = []; 
    for (let i = 0; i < 600; i ++) {
        let radius = (Math.random()*3) + 1 ; 
        let x = Math.random() * (window.innerWidth - 2*radius) + radius; 
        let y = Math.random() * (window.innerHeight - 2*radius) + radius; 
        let dx = (Math.random()-0.5)*0.3 ; 
        let dy = (Math.random()-0.5)*0.3; 


        //to pick a good color palette, go to color.adobe.com
        let colArr = ["#220B5E", "#000428", "#3B1D98", "navy", "#000929"]
        circleArr.push(new Circle(x, y, radius, dx, dy,colArr[Math.floor(Math.random() * colArr.length)] )); 
    }
}
function animate() {
    requestAnimationFrame(animate);
    //clear the canvas
    c.clearRect(0,0, window.innerWidth, window.innerHeight); 
    circleArr.forEach((circ) => {
        circ.update(); 
    }
    )
}
init(); 
animate()


