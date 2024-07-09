var sortBtn = document.querySelector('.filter-menu').children;
var sortItem = document.querySelectorAll('.row>div');
console.log(sortBtn, sortItem);

for (var i = 0; i < sortBtn.length; i++) {

    sortBtn[i].addEventListener('click', function () {
        // removing class current from all li items of ul class filter-menu
        for (var j = 0; j < sortBtn.length; j++) {
            //removing currect class from all buttons
            sortBtn[j].classList.remove('current');
        }

        console.log(this);
        //this is regering to sortBtn[i]
        this.classList.add('current');

        var targetData = this.getAttribute('data-target');//getting the data-target value
        // console.log(targetData);// data-target value will be displayed e.g. js

        for (var k = 0; k < sortItem.length; k++) {
            sortItem[k].classList.remove('active');
            sortItem[k].classList.add('delete');

            // console.log(sortItem[k].getAttribute('data-item')); 
            if (sortItem[k].getAttribute('data-item') == targetData || targetData == "Reset") {
                sortItem[k].classList.remove('delete');
                sortItem[k].classList.add('active');
            }
        }
    });
}