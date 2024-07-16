document.addEventListener('DOMContentLoaded', function(){
//    const newsLink = document.getElementById('news-link');
//    const emailSpamLink = document.getElementById('email-spam-link');
//    const moreInfoLink = document.getElementById('more-info-link');
//    const newsSection = document.getElementById('news-section');
//    const emailSpamSection = document.getElementById('email-spam-section');
//    const moreInfoSection = document.getElementById('more-info-section');
//
//    function showSection(section){
//        newsSection.classList.remove('active');
//        emailSpamSection.classList.remove('active');
//        moreInfoSection.classList.remove('active');
//        newsLink.classList.remove('active');
//        emailSpamLink.classList.remove('active');
//        moreInfoLink.classList.remove('active');
//
//        if (section === 'news') {
//            newsSection.classList.add('active');
//            newsLink.classList.add('active');
//        } else if (section === 'email-spam') {
//            emailSpamSection.classList.add('active');
//            emailSpamLink.classList.add('active');
//        } else if (section === 'more-info') {
//            moreInfoSection.classList.add('active');
//            moreInfoLink.classList.add('active');
//        }
//
//        document.querySelector('.main-right').scrollTop = 0;
//    }
//
//    newsLink.addEventListener('click', function (e) {
//        e.preventDefault();
//        showSection('news');
//    });
//
//    emailSpamLink.addEventListener('click', function (e) {
//        e.preventDefault();
//        showSection('email-spam');
//    });
//
//    moreInfoLink.addEventListener('click', function(e) {
//        e.preventDefault();
//        showSection('more-info');
//    })
//
//    // Initially show the news section
//    showSection('news');

    const button = document.getElementById('email-predict-btn');
    button.addEventListener('click', function() {
        this.classList.toggle('active');
        setTimeout(() => {
            this.classList.remove('active');
        }, 100); // Remove the class after 0.5 seconds
    });
})
