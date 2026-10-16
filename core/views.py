from django.shortcuts import render


def home_page(request):
    return render(request, "home_page.html")


# services pages


def affiliate_marketing_page(request):
    return render(request, "services/affiliate_marketing_page.html")


def app_development_page(request):
    context = {
        "tech_stack": [
            {
                "name": "Swift",
                "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/swift/swift-original.svg",
            },
            {
                "name": "Kotlin",
                "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kotlin/kotlin-original.svg",
            },
            {
                "name": "Flutter",
                "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flutter/flutter-original.svg",
            },
            {
                "name": "React",
                "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg",
            },
            {
                "name": "Firebase",
                "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/firebase/firebase-plain.svg",
            },
            {
                "name": "GraphQL",
                "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/graphql/graphql-plain.svg",
            },
            {
                "name": "Android",
                "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/android/android-original.svg",
            },
            {
                "name": "Google Cloud",
                "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg",
            },
            {
                "name": "TypeScript",
                "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg",
            },
            {
                "name": "SQLite",
                "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg",
            },
            {
                "name": "Figma",
                "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg",
            },
            {
                "name": "Apple",
                "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apple/apple-original.svg",
            },
        ],
        "industries": [
            {
                "title": "Healthcare & Telehealth",
                "desc": "HIPAA-compliant patient portals, secure messaging, and wearable medical device telemetry integration.",
                "icon": "M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z",
            },
            {
                "title": "Fintech & Mobile Banking",
                "desc": "Secure biometric login, contactless payments, micro-investing, and real-time push transaction alerts.",
                "icon": "M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
            },
            {
                "title": "Retail & E-Commerce Apps",
                "desc": "Immersive shopping interfaces, loyalty wallets, personalized recommendations, and instant push promotions.",
                "icon": "M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z",
            },
            {
                "title": "Logistics & Field Operations",
                "desc": "Offline-capable driver routing apps, barcode scanning tools, barcode tracking, and real-time dispatch systems.",
                "icon": "M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0zM13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1",
            },
        ],
        "capabilities": [
            {
                "title": "Native iOS &amp; Android",
                "desc": "Swift and Kotlin builds for teams that need maximum performance and full platform access.",
                "img": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=1000&auto=format&fit=crop&q=80",
            },
            {
                "title": "Cross-Platform Apps",
                "desc": "Flutter and React Native builds that ship to both stores from a single, maintainable codebase.",
                "img": "https://images.unsplash.com/photo-1551650975-87deedd944c3?w=1000&auto=format&fit=crop&q=80",
            },
            {
                "title": "UX &amp; Interaction Design",
                "desc": "Wireframes through high-fidelity prototypes, tested with real users before a line of code ships.",
                "img": "https://images.unsplash.com/photo-1523800503107-5bc3ba2a6f81?w=1000&auto=format&fit=crop&q=80",
            },
            {
                "title": "Backend &amp; API Integration",
                "desc": "Scalable backends, push notifications, and secure integrations with your existing systems.",
                "img": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1000&auto=format&fit=crop&q=80",
            },
            {
                "title": "QA &amp; Device Testing",
                "desc": "Real-device testing across screen sizes, OS versions and network conditions.",
                "img": "https://images.unsplash.com/photo-1571171637578-41bc2dd41cd2?w=1000&auto=format&fit=crop&q=80",
            },
            {
                "title": "App Store Management",
                "desc": "Submission, ASO, and version rollouts handled end-to-end, plus ongoing maintenance after launch.",
                "img": "https://images.unsplash.com/photo-1616469829581-73993eb86b02?w=1000&auto=format&fit=crop&q=80",
            },
        ],
    }
    return render(request, "what-we-do/app_development_page.html", context)


def content_marketing_page(request):
    return render(request, "services/content_marketing_page.html")


def email_marketing_page(request):
    return render(request, "services/email_marketing_page.html")


def influencer_marketing_page(request):
    return render(request, "services/influencer_marketing_page.html")


def seo_page(request):
    return render(request, "services/seo_page.html")


def social_media_marketing_page(request):
    return render(request, "services/social_media_marketing_page.html")


def social_media_marketing_page(request):
    return render(request, "services/social_media_marketing_page.html")


def software_development_page(request):
    return render(request, "services/software_development_page.html")


def ux_ui_page(request):
    return render(request, "services/ux_ui_page.html")


def web_development_page(request):

    industries_raw = [
        {
            "title": "Banking & Financial Services",
            "desc": "Open banking architectures, secure portal infrastructure, and high-throughput transaction engines.",
            "icon": "M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
        },
        {
            "title": "Healthcare & Life Sciences",
            "desc": "HIPAA-compliant engagement portals, tele-health platforms, and clinical system integrations.",
            "icon": "M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z",
        },
        {
            "title": "Retail & Digital Commerce",
            "desc": "Headless commerce ecosystems built for extreme traffic spikes, global localization, and omni-channel delivery.",
            "icon": "M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z",
        },
        {
            "title": "Manufacturing & Logistics",
            "desc": "B2B ordering engines, IoT integration dashboards, and real-time global supply chain tracking portals.",
            "icon": "M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0zM13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1",
        },
    ]

    industries = [
        {**ind, "stagger": (i % 4) + 1} for i, ind in enumerate(industries_raw)
    ]

    tech_stack = [
        {
            "name": "laravel",
            "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/laravel/laravel-original.svg",
        },
        {
            "name": "react",
            "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg",
        },
        {
            "name": "nodejs",
            "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg",
        },
        {
            "name": "vuejs",
            "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg",
        },
        {
            "name": "nextjs",
            "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg",
        },
        {
            "name": "typescript",
            "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg",
        },
        {
            "name": "tailwindcss",
            "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-original.svg",
        },
        {
            "name": "graphql",
            "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/graphql/graphql-plain.svg",
        },
        {
            "name": "docker",
            "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg",
        },
        {
            "name": "aws",
            "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg",
        },
        {
            "name": "mongodb",
            "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg",
        },
        {
            "name": "postgresql",
            "url": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg",
        },
    ]

    capabilities_raw = [
        {
            "title": "Custom Web Applications",
            "desc": "Bespoke platforms built around complex enterprise workflows &mdash; from internal operational consoles to customer portals.",
            "img": "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1000&auto=format&fit=crop&q=80",
        },
        {
            "title": "Headless & DXP Architecture",
            "desc": "Decoupled content and commerce platforms enabling unified digital experience delivery across global brands.",
            "img": "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?w=1000&auto=format&fit=crop&q=80",
        },
        {
            "title": "API & ERP Systems Integration",
            "desc": "Enterprise service bus (ESB) and microservices layer connecting web platforms to SAP, Salesforce, and legacy core systems.",
            "img": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1000&auto=format&fit=crop&q=80",
        },
        {
            "title": "Progressive Web Apps (PWA)",
            "desc": "App-like enterprise web solutions operating seamlessly offline, with instant updates and low latency.",
            "img": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=1000&auto=format&fit=crop&q=80",
        },
        {
            "title": "Application Modernization",
            "desc": "Refactoring legacy ASP.NET or PHP systems into containerized, cloud-native micro-frontends with continuous uptime.",
            "img": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1000&auto=format&fit=crop&q=80",
        },
        {
            "title": "Cloud-Native Micro-Frontends",
            "desc": "Decoupled UI components empowering independent teams to deploy features faster without monolithic bottlenecks.",
            "img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1000&auto=format&fit=crop&q=80",
        },
        {
            "title": "Enterprise Content Management (CMS)",
            "desc": "Scalable implementation of robust CMS ecosystems (Strapi, WordPress, Contentful) configured for multi-site global enterprises.",
            "img": "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=1000&auto=format&fit=crop&q=80",
        },
        {
            "title": "Web Performance & SEO Optimization",
            "desc": "Deep Core Web Vitals optimization, advanced caching strategies, and technical SEO structure to drive search visibility.",
            "img": "https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?w=1000&auto=format&fit=crop&q=80",
        },
        {
            "title": "24/7 Managed Services & SLAs",
            "desc": "L1-L3 support desk, active infrastructure telemetry, automated vulnerability patching, and guaranteed uptime SLAs.",
            "img": "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=1000&auto=format&fit=crop&q=80",
        },
    ]
    capabilities = [
        {**c, "stagger": (i % 3) + 1} for i, c in enumerate(capabilities_raw)
    ]

    use_cases = [
        {
            "tech": "Laravel",
            "title": "Secure Customer Portals",
            "desc": "Role-based access, audit trails, and encrypted data flows for regulated industries.",
            "img": "https://images.unsplash.com/photo-1517430816045-df4b7de11d1d?w=900&auto=format&fit=crop&q=80",
        },
        {
            "tech": "React / Next.js",
            "title": "Real-Time Dashboards",
            "desc": "Streaming data visualizations for operations teams monitoring live infrastructure.",
            "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=900&auto=format&fit=crop&q=80",
        },
        {
            "tech": "Node.js",
            "title": "High-Throughput APIs",
            "desc": "Event-driven services handling thousands of concurrent transactions with low latency.",
            "img": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=900&auto=format&fit=crop&q=80",
        },
        {
            "tech": "GraphQL",
            "title": "Unified Data Layer",
            "desc": "Single query interface aggregating data across microservices and legacy systems.",
            "img": "https://images.unsplash.com/photo-1516110833967-0b5716ca1387?w=900&auto=format&fit=crop&q=80",
        },
        {
            "tech": "Docker & AWS",
            "title": "Global Cloud Deployment",
            "desc": "Containerized workloads orchestrated across multi-region clusters for resilience.",
            "img": "https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=900&auto=format&fit=crop&q=80",
        },
        {
            "tech": "MongoDB / PostgreSQL",
            "title": "Adaptive Data Modeling",
            "desc": "Hybrid relational and document stores tuned for both structure and scale.",
            "img": "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=900&auto=format&fit=crop&q=80",
        },
    ]

    process_steps = [
        {
            "step": "01",
            "title": "Consult & Blueprint",
            "desc": "Technical discovery, compliance scoping, and target solution architecture defined.",
            "img": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=1600&auto=format&fit=crop&q=80",
        },
        {
            "step": "02",
            "title": "Architect & Plan",
            "desc": "Microservices design, API blueprints, and sprint roadmaps established.",
            "img": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1600&auto=format&fit=crop&q=80",
        },
        {
            "step": "03",
            "title": "DevSecOps Build",
            "desc": "Agile sprints paired with continuous automated code review and SAST scanning.",
            "img": "https://images.unsplash.com/photo-1550439062-609e1531270e?w=1600&auto=format&fit=crop&q=80",
        },
        {
            "step": "04",
            "title": "Test & Assurance",
            "desc": "Penetration testing, accessibility audits, and staged multi-region deployments.",
            "img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1600&auto=format&fit=crop&q=80",
        },
        {
            "step": "05",
            "title": "SLA & Evolution",
            "desc": "24/7 active telemetry, incident management, and continuous optimization.",
            "img": "https://images.unsplash.com/photo-1487014679447-9f8336841d58?w=1600&auto=format&fit=crop&q=80",
        },
    ]
    return render(
        request,
        "what-we-do/web_development_page.html",
        {
            "tech_stack": tech_stack,
            "industries": industries,
            "capabilities": capabilities,
            "use_cases": use_cases,
            "process_steps": process_steps,
        },
    )


# industires pages


def banking_and_finance_page(request):
    return render(request, "industries/banking_and_finance_page.html")


def education_page(request):
    return render(request, "industries/education_page.html")


def education_page(request):
    return render(request, "industries/education_page.html")
