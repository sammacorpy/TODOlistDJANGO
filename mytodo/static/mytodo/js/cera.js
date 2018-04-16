
$('document').ready(function() {
    $('.navbtn').click(function() {
        $('.listnavitems').toggleClass('shows');
        $('.hamburg').toggleClass('shows');
        $('listnavitems>a').toggleClass('shows')
    });


    var imga = document.getElementById("quotespic");
    var aadj = window.innerWidth
    if (window.innerHeight < window.innerWidth) {
        aadj = window.innerHeight;
    }

    if (window.innerWidth < 550) {
        aadj = window.innerWidth;
    }

    imga.width = aadj * 0.9;
    imga.height = aadj * 0.58;





    window.addEventListener('resize', function() {
        var aadj = window.innerWidth
        if (window.innerHeight < window.innerWidth) {
            aadj = window.innerHeight;
        }
        if (window.innerWidth < 550) {
            aadj = window.innerWidth;
        }

        imga.width = aadj * 0.9;
        imga.height = aadj * 0.58;

    });

    function logoanimation() {
        var canvas = document.getElementById('logring');
        var c = canvas.getContext("2d");


        c.lineWidth = "4";

        var x = 0;
        var y = 0;


        function animate() {
            requestAnimationFrame(animate);
            c.clearRect(0, 0, canvas.width, canvas.height);


            c.beginPath();
            c.arc(canvas.width / 2, canvas.height / 2, 70, x + 0, x + 1.5 * 3.14, false);
            c.strokeStyle = "#050259";
            c.stroke();

            c.beginPath();
            c.arc(canvas.width / 2, canvas.height / 2, 55, y + 3.14, y + 2.5 * 3.14, false);
            c.strokeStyle = "#1B21A6";
            c.stroke();

            c.beginPath();
            c.arc(canvas.width / 2, canvas.height / 2, 40, x + 0, x + 1.5 * 3.14, false);
            c.strokeStyle = "#010440";
            c.stroke();

            x += 0.05;
            y -= 0.05;

            if (x > 2 * Math.PI) {
                x = 0;
            }

            if (y < -(2 * Math.PI)) {
                y = 0;
            }
        }
        animate();
    }
    logoanimation();








































});