/*Chewy Chupucabras :: Ethan Sie, Tanzeem Hasan, Brian Liu
SoftDev pd4
K28 -- Manipulating the DOM
2025-01-07t
 */


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x)
{
    var j=30;
    return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
              return x+30;
          }
        };

//create a new node in the tree
var addItem = function(text)
{
    var list = document.getElementById("thelist");
    /* console.log(list); */
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};

//prune a node from the tree
var removeItem = function(n)
{
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove();
};

//color selected elements red
var red = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	     items[i].classList.add('red');
    }
    console.log(items)

};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	     if (i%2==0) {
	        items[i].classList.add('red');
	      } else {
	         items[i].classList.add('blue');
	       }
    }
    console.log(items) //a lot of information other than just the items when trying to print in the console
};


//insert your implementations here for...
function fac(n) {
    if (n === 0) {
      return 1;
    }
    return n * fac(n - 1);
  }
  
function fib(n) {
    if (n <= 1) {
      return n;
    }
    return fib(n - 1) + fib(n - 2);
  }
function gcd(a, b) {
    if (b == 0) {
        return a;
    };
    return gcd(b, a % b);
  };

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (a, b) => {
    if (b == 0) {
        return a;
    };
    return myFxn(b, a % b);
};

addItem(myFxn(120,20))
