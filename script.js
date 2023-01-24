var posts = ["slide 1", "slide 2", "slide 3", "slide 4"] //each thread has its own posts

function load_init_posts() {
	var str = '<ul>'

	posts.forEach(function(slide) {
	  str += '<li>'+ slide + '</li>';
	}); 

	str += '</ul>';
	document.getElementById("slideContainer").innerHTML = str;
}

function submit_post() {
	posts.push("slide 5")
	load_init_posts()
}