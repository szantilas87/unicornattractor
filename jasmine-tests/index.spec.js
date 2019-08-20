describe('_navbar.html', function() {
    beforeEach(function() {
        jasmine.getFixtures().fixturesPath = '/templates/partials/';
        loadFixtures('_navbar.html');
    });

    describe('navbar', function() {
        it('should contains class navbar', function() {
            expect($('.navbar')).toBeInDOM();
        });
        it('should have a active link in the logo', function() {
            expect($('.navbar-brand')).toBeInDOM();
            var spyEvent = spyOnEvent('.navbar-brand', 'click');
            $('.navbar-brand').click();
            expect('click').toHaveBeenTriggeredOn('.navbar-brand');
            expect(spyEvent).toHaveBeenTriggered();
        });

        it('should have active drop down menu', function() {
            var spyEvent = spyOnEvent('.navbar-toggler', 'click');
            $('.navbar-toggler').click();
            expect('click').toHaveBeenTriggeredOn('.navbar-toggler');
            expect(spyEvent).toHaveBeenTriggered();
            expect($('<a class="navbar-brand">UnicornAttractor</a>')).toContainText('UnicornAttractor')
        });

        it('should contains 9 tabs', function() {
            expect($('.navbar-nav > li')).toHaveLength(9);
            expect($('<a class="nav-link">Home</a>')).toContainText('Home')
            expect($('<a class="nav-link">About</a>')).toContainText('About')
            expect($('<a class="nav-link">Contact</a>')).toContainText('Contact')
            expect($('<a class="nav-link">Bugs</a>')).toContainText('Bugs')
            expect($('<a class="nav-link">Features</a>')).toContainText('Features')
            expect($('<a class="nav-link">Profile</a>')).toContainText('Profile')
            expect($('<a class="nav-link">Logout</a>')).toContainText('Logout')
            expect($('<a class="nav-link">Login</a>')).toContainText('Login')
            expect($('<a class="nav-link">Register</a>')).toContainText('Register')
        });
    });
});

describe('index.html', function() {
    beforeEach(function() {
        jasmine.getFixtures().fixturesPath = '/templates/pages/';
        loadFixtures('index.html');
    });

    describe('showcase', function() {
        it('should contains section showcase', function() {
            expect($('<section id="showcase"></section>')).toHaveId("showcase")
        });
        it('should have a div with class showcase-left', function() {
            expect($('.showcase-left')).toBeInDOM()
        });
        it('should have one image in showcase-left', function() {
            expect($('.showcase-left > img')).toHaveLength(1)
        });
        it('should have h1 with a text in showcase-left', function() {
            expect($('<h1>WE WILL FIX ALL YOUR BUGS</h1>')).toHaveText('WE WILL FIX ALL YOUR BUGS')
        });
    });

    describe('bugs-info', function() {
        it('should contains section bugs-info', function() {
            expect($('<section id="bugs-info"></section>')).toHaveId("bugs-info")
        });
        it('should have a div with class bugs-left', function() {
            expect($('.bugs-left')).toBeInDOM()
        });
        it('should have h3 with a text in bugs-left', function() {
            expect($('<h3>BROWSE THROUGH EXISTING BUGS</h3>')).toHaveText('BROWSE THROUGH EXISTING BUGS')
        });
        it('should have a div with class bugs-right', function() {
            expect($('.bugs-right')).toBeInDOM()
        });
        it('should have h1 with a text in bugs-right', function() {
            expect($('<h3>ADD A NEW BUG</h3>')).toHaveText('ADD A NEW BUG')
        });
    });

    describe('testimonials', function() {
        it('should contains section testimonials', function() {
            expect($('<section id="testimonials"></section>')).toHaveId("testimonials")
        });
        it('should have h2 with a text in testimonials', function() {
            expect($(' <h2>Our customers said about us:</h2>')).toHaveText('Our customers said about us:')
        });
        it('should have four customer cards', function() {
            expect($('.card-customer')).toHaveLength(4)
        });
        it('should have profile picture and background picture for every cutomer card', function() {
            expect($('.card-customer > img')).toHaveLength(8)
        });
    });


    describe('features', function() {
        it('should contains section features', function() {
            expect($('<section id="features"></section>')).toHaveId("features")
        });
        it('should have a div with class info-left', function() {
            expect($('.info-left')).toBeInDOM()
        });
        it('should have one image in info-right', function() {
            expect($('.info-right > img')).toHaveLength(1)
        });
        it('should have h1 with a text in bugs-left', function() {
            expect($('<h1>WE WILL DEVELOP SOPHISTICATED FEATURES FOR YOU</h1>')).toHaveText('WE WILL DEVELOP SOPHISTICATED FEATURES FOR YOU')
        });
    });

    describe('features-info', function() {
        it('should contains section features-info', function() {
            expect($('<section id="features-info"></section>')).toHaveId("features-info")
        });
        it('should have a div with class features-left', function() {
            expect($('.features-left')).toBeInDOM()
        });
        it('should have h3 with a text in features-left', function() {
            expect($('<h3>CHECK THE FEATURES WE WORK ON</h3>')).toHaveText('CHECK THE FEATURES WE WORK ON')
        });
        it('should have a div with class features-right', function() {
            expect($('.features-right')).toBeInDOM()
        });
        it('should have h1 with a text in features-right', function() {
            expect($('<h3>ADD A NEW FEATURE</h3>')).toHaveText('ADD A NEW FEATURE')
        });
    });

    describe('contact', function() {
        it('should contains section contact', function() {
            expect($('<section id="contact"></section>')).toHaveId("contact")
        });
        it('should have one form', function() {
            expect($('#contact form')).toHaveLength(1)
        });
    });
});

describe('_footer.html', function() {
    beforeEach(function() {
        jasmine.getFixtures().fixturesPath = '/templates/partials/';
        loadFixtures('_footer.html');
    });

    describe('footer-top', function() {
        it('should contains div footer-top', function() {
            expect($('<div class="footer-top"></div>')).toHaveClass("footer-top")
        });
        it("should have h3 'About'", function() {
            expect($('<h3>About</h3>')).toHaveText('About')
        });
        it('should have four links in the footer', function() {
            expect($('#links > li')).toHaveLength(4)
        });
        it("should have h2 'Our newsletter'", function() {
            expect($('<h2>Our newsletter</h2>')).toHaveText('Our newsletter')
        });
        it('should have one form', function() {
            expect($('.footer-top form')).toHaveLength(1)
        });
        it('should have four links to social media', function() {
            expect($('.footer-top i')).toHaveLength(4)
        });
    });
});