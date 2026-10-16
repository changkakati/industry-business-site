document.addEventListener('DOMContentLoaded', function () {

    // 1. INITIAL HERO ANIMATIONS
    setTimeout(() => {
        document.querySelectorAll('.hero-anim').forEach(el => {
            el.classList.remove('reveal-hidden');
        });
    }, 100);

    // 2. SCROLL REVEALS USING INTERSECTION OBSERVER
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -10% 0px',
        threshold: 0.1
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.remove('reveal-hidden');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.scroll-reveal').forEach(el => {
        revealObserver.observe(el);
    });

    // 3. COUNTER NUMBERS
    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('[data-counter]').forEach(el => {
        counterObserver.observe(el);
    });

    function animateCounter(el) {
        const targetValue = parseFloat(el.getAttribute('data-counter') || '0');
        const suffix = el.getAttribute('data-suffix') || '';
        const isDecimal = el.getAttribute('data-counter').includes('.');
        const decimals = isDecimal ? el.getAttribute('data-counter').split('.')[1].length : 0;

        const duration = 1600;
        const startTime = performance.now();

        function updateCounter(currentTime) {
            const elapsedTime = currentTime - startTime;
            const progress = Math.min(elapsedTime / duration, 1);

            const easeOutQuart = 1 - Math.pow(1 - progress, 4);
            const currentVal = targetValue * easeOutQuart;

            el.textContent = isDecimal ?
                currentVal.toFixed(decimals) + suffix :
                Math.round(currentVal) + suffix;

            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                el.textContent = (isDecimal ? targetValue.toFixed(decimals) : targetValue) + suffix;
            }
        }

        requestAnimationFrame(updateCounter);
    }

    // 4. ARCHITECTURE TABS SWITCHER
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetId = button.getAttribute('data-target');

            tabButtons.forEach(btn => {
                btn.classList.remove('active', 'border-blue-600', 'bg-blue-600',
                    'text-white');
                btn.classList.add('border-gray-200', 'bg-white', 'text-slate-700');
            });

            button.classList.add('active', 'border-blue-600', 'bg-blue-600', 'text-white');
            button.classList.remove('border-gray-200', 'bg-white', 'text-slate-700');

            tabContents.forEach(content => {
                if (content.id === targetId) {
                    content.classList.remove('hidden');
                    content.classList.add('block', 'tab-fade-in');
                } else {
                    content.classList.remove('block', 'tab-fade-in');
                    content.classList.add('hidden');
                }
            });
        });
    });

    // 5. FAQ ACCORDION
    document.querySelectorAll('.faqToggle').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const item = btn.closest('.faqItem');
            const body = item.querySelector('.faqBody');
            const icon = item.querySelector('.faqIcon');
            const isOpen = item.classList.contains('is-open');

            document.querySelectorAll('.faqItem.is-open').forEach(function (openItem) {
                if (openItem !== item) {
                    openItem.classList.remove('is-open');
                    const openBody = openItem.querySelector('.faqBody');
                    const openIcon = openItem.querySelector('.faqIcon');

                    openBody.style.height = openBody.scrollHeight + 'px';
                    void openBody.offsetHeight;
                    openBody.style.height = '0px';
                    openIcon.style.transform = 'rotate(0deg)';
                }
            });

            if (isOpen) {
                item.classList.remove('is-open');
                body.style.height = body.scrollHeight + 'px';
                void body.offsetHeight;
                body.style.height = '0px';
                icon.style.transform = 'rotate(0deg)';
            } else {
                item.classList.add('is-open');
                body.style.height = body.scrollHeight + 'px';
                icon.style.transform = 'rotate(180deg)';

                setTimeout(() => {
                    if (item.classList.contains('is-open')) {
                        body.style.height = 'auto';
                    }
                }, 300);
            }
        });
    });
    // 6. TECHNOLOGY USE CASES CAROUSEL
    const useCaseTrack = document.getElementById('useCaseTrack');
    const useCasePrev = document.getElementById('useCasePrev');
    const useCaseNext = document.getElementById('useCaseNext');

    if (useCaseTrack && useCasePrev && useCaseNext) {
        useCasePrev.addEventListener('click', () => {
            useCaseTrack.scrollBy({
                left: -360,
                behavior: 'smooth'
            });
        });
        useCaseNext.addEventListener('click', () => {
            useCaseTrack.scrollBy({
                left: 360,
                behavior: 'smooth'
            });
        });
    }

    // 7. KEY FACTS MULTI-SLIDER
    const factsTrack = document.getElementById('factsTrack');
    const factsDots = document.querySelectorAll('#factsDots button');
    const factPrev = document.getElementById('factPrev');
    const factNext = document.getElementById('factNext');

    if (factsTrack && factsDots.length > 0) {
        let currentFactIndex = 0;
        const totalFactSlides = factsTrack.children.length;

        function getVisibleFactSlides() {
            if (window.innerWidth >= 1024) return 3;
            if (window.innerWidth >= 768) return 2;
            return 1;
        }

        function getMaxFactIndex() {
            return Math.max(0, totalFactSlides - getVisibleFactSlides());
        }

        function updateFactSlide(index) {
            const maxIndex = getMaxFactIndex();
            currentFactIndex = Math.min(Math.max(index, 0), maxIndex);
            const percentPerSlide = 100 / getVisibleFactSlides();
            factsTrack.style.transform = `translateX(-${currentFactIndex * percentPerSlide}%)`;

            factsDots.forEach((dot, idx) => {
                if (idx === currentFactIndex) {
                    dot.classList.remove('bg-gray-300');
                    dot.classList.add('bg-blue-600');
                } else {
                    dot.classList.remove('bg-blue-600');
                    dot.classList.add('bg-gray-300');
                }
            });
        }

        if (factNext) {
            factNext.addEventListener('click', () => updateFactSlide(currentFactIndex + 1));
        }
        if (factPrev) {
            factPrev.addEventListener('click', () => updateFactSlide(currentFactIndex - 1));
        }
        factsDots.forEach(dot => {
            dot.addEventListener('click', function () {
                updateFactSlide(parseInt(this.getAttribute('data-slide')));
            });
        });

        window.addEventListener('resize', () => updateFactSlide(currentFactIndex));
        updateFactSlide(0);
    }
});