// get all main links
const mainLinks = document.querySelectorAll('.main-blocks');

// add event listener to each main link
mainLinks.forEach(link => {
  link.addEventListener('click', (event) => {
    // prevent default behavior of link click
    event.preventDefault();
    
    // get sub-blocks for this main link
    const subBlocks = link.nextElementSibling;

    // toggle visibility of sub-blocks
    subBlocks.style.display = subBlocks.style.display === 'none' ? 'block' : 'none';

    // hide sub-blocks of other main links
    mainLinks.forEach(otherLink => {
      if (otherLink !== link) {
        otherLink.nextElementSibling.style.display = 'none';
      }
    });


/* show/hide body blocks depending on clicked main-block*/
    // get the ID of the corresponding body text
    const target = link.dataset.target;

    // select the corresponding body text element
    const bodyText = document.getElementById(target);

    // show the selected body text element and hide others
    document.querySelectorAll('.body-text').forEach(text => {
      if (text === bodyText) {
        text.style.display = 'block';
      } else {
        text.style.display = 'none';
      }
    });
  });
});

// get all nav links
const navLinks = document.querySelectorAll('.nav-item');

// add event listener to each nav link
navLinks.forEach(link => {
  link.addEventListener('click', () => {
    // remove active class from all nav links
    navLinks.forEach(otherLink => {
      otherLink.classList.remove('active');
    });

    // add active class to clicked nav link
    link.classList.add('active');
  });
});

