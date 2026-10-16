document.addEventListener('DOMContentLoaded', function () {

    // 1. Interactive Mouse Light Tracking on Hero Card
    const heroCard = document.querySelector('.hero-card');
    if (heroCard) {
        heroCard.addEventListener('mousemove', (e) => {
            const rect = heroCard.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            heroCard.style.setProperty('--mouse-x', `${x}px`);
            heroCard.style.setProperty('--mouse-y', `${y}px`);
        });
    }


    // 2. Parallax Scrolling on Floating Glow Blobs
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        const heroGlow1 = document.querySelector('.hero-light');
        const heroGlow2 = document.querySelector('.hero-light2');

        if (scrolled < 1000) {
            if (heroGlow1) heroGlow1.style.transform = `translateY(${scrolled * 0.15}px)`;
            if (heroGlow2) heroGlow2.style.transform = `translateY(${scrolled * -0.1}px)`;
        }
    }, {
        passive: true
    });


    // 3. Architecture Tab Switcher Handler (Adapted for Light Theme)
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            document.querySelectorAll('.tab-btn').forEach(b => {
                b.classList.remove('bg-blue-600', 'text-white', 'border-blue-600',
                    'active');
                b.classList.add('border-gray-200', 'bg-white', 'text-slate-700');
            });
            this.classList.add('bg-blue-600', 'text-white', 'border-blue-600', 'active');
            this.classList.remove('border-gray-200', 'bg-white', 'text-slate-700');

            const target = this.dataset.target;
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.toggle('hidden', content.id !== target);
            });
        });
    });


    // 4. Native IntersectionObserver for Scroll Reveals
    const revealElements = document.querySelectorAll('.reveal-element');
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15
    });

    revealElements.forEach(el => revealObserver.observe(el));


    // 5. Number Counter Animation
    const counters = document.querySelectorAll('[data-counter]');
    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const rawTarget = el.getAttribute('data-counter');
                const target = parseFloat(rawTarget);
                const suffix = el.getAttribute('data-suffix') || '';
                const isDecimal = rawTarget.includes('.');
                const decimals = isDecimal ? rawTarget.split('.')[1].length : 0;

                let start = 0;
                const duration = 1600;
                const startTime = performance.now();

                function updateCounter(currentTime) {
                    const elapsed = currentTime - startTime;
                    const progress = Math.min(elapsed / duration, 1);
                    const easeProgress = 1 - Math.pow(1 - progress, 3);
                    const currentVal = start + (target - start) * easeProgress;

                    el.textContent = isDecimal ?
                        currentVal.toFixed(decimals) + suffix :
                        Math.round(currentVal) + suffix;

                    if (progress < 1) requestAnimationFrame(updateCounter);
                }

                requestAnimationFrame(updateCounter);
                observer.unobserve(el);
            }
        });
    }, {
        threshold: 0.5
    });

    counters.forEach(counter => counterObserver.observe(counter));


    // 6. FAQ Accordion Handler
    document.querySelectorAll('.faqToggle').forEach(button => {
        button.addEventListener('click', function () {
            const item = this.closest('.faqItem');
            if (!item) return;

            const body = item.querySelector('.faqBody');
            const icon = item.querySelector('.faqIcon');
            const isOpen = body.style.maxHeight && body.style.maxHeight !== '0px';

            document.querySelectorAll('.faqBody').forEach(b => b.style.maxHeight = '0px');
            document.querySelectorAll('.faqIcon').forEach(i => i.style.transform =
                'rotate(0deg)');

            if (!isOpen && body) {
                body.style.maxHeight = body.scrollHeight + 'px';
                if (icon) icon.style.transform = 'rotate(180deg)';
            }
        });
    });


    // 7. Carousel Controls (Use Cases)
    const useCaseTrack = document.getElementById('useCaseTrack');
    const useCasePrev = document.getElementById('useCasePrev');
    const useCaseNext = document.getElementById('useCaseNext');

    if (useCaseTrack && useCasePrev && useCaseNext) {
        const scrollByCard = (direction) => {
            const card = useCaseTrack.querySelector('.useCaseCard');
            const gap = 24;
            const amount = card ? card.offsetWidth + gap : 320;

            useCaseTrack.scrollBy({
                left: direction * amount,
                behavior: 'smooth'
            });
        };

        useCasePrev.addEventListener('click', () => scrollByCard(-1));
        useCaseNext.addEventListener('click', () => scrollByCard(1));
    }


    // 8. Delivery Governance Slider
    const deliveryTrack = document.getElementById('deliveryTrack');
    const deliveryPrev = document.getElementById('deliveryPrev');
    const deliveryNext = document.getElementById('deliveryNext');
    const deliveryDots = document.querySelectorAll('#deliveryDots button');

    if (deliveryTrack && deliveryPrev && deliveryNext && deliveryDots.length > 0) {

        const slides = deliveryTrack.children;
        let currentSlide = 0;

        function updateDeliverySlider() {
            deliveryTrack.style.transform =
                `translateX(-${currentSlide * 100}%)`;

            deliveryDots.forEach((dot, index) => {
                if (index === currentSlide) {
                    dot.classList.remove('w-2.5', 'bg-white/40');
                    dot.classList.add('w-6', 'bg-blue-500');
                } else {
                    dot.classList.remove('w-6', 'bg-blue-500');
                    dot.classList.add('w-2.5', 'bg-white/40');
                }
            });
        }

        deliveryNext.addEventListener('click', function () {
            currentSlide++;

            if (currentSlide >= slides.length) {
                currentSlide = 0;
            }

            updateDeliverySlider();
        });

        deliveryPrev.addEventListener('click', function () {
            currentSlide--;

            if (currentSlide < 0) {
                currentSlide = slides.length - 1;
            }

            updateDeliverySlider();
        });

        deliveryDots.forEach((dot, index) => {
            dot.addEventListener('click', function () {
                currentSlide = index;
                updateDeliverySlider();
            });
        });

        updateDeliverySlider();
    }

});


