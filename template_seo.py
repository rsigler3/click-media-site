import re

with open('/Volumes/Speedy Disk/click-media-site/social-media.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I want to extract everything before the header and everything after the main content so I can inject the new SEO content.
header_end = content.find('<header class="relative')
footer_start = content.find('<footer')

if header_end != -1 and footer_start != -1:
    top = content[:header_end]
    bottom = content[footer_start:]
    print("Found header and footer")
    
    # We will need to replace the title and description in the top section
    top = re.sub(r'<title>.*?</title>', '<title>SEO Services Jamestown NY | Search Engine Optimization Experts</title>', top)
    top = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="Get found on the first page of Google. We provide data-driven SEO services in Jamestown, NY, to help your business increase traffic, leads, and local visibility." />', top)
    
    # Also update the JSON-LD schema
    schema = """{
  "@context": "https://schema.org/",
  "@type": "Service",
  "serviceType": "Search Engine Optimization",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Click Media and Marketing"
  },
  "areaServed": {
    "@type": "State",
    "name": "New York"
  },
  "description": "Get found on the first page of Google. We provide data-driven SEO services in Jamestown, NY, to help your business increase traffic, leads, and local visibility.",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "SEO Services",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Technical SEO"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "On-Page Optimization"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Local SEO & Google Maps"
        }
      }
    ]
  }
}"""
    top = re.sub(r'<script type="application/ld\+json">.*?</script>', f'<script type="application/ld+json">\n{schema}\n</script>', top, flags=re.DOTALL)

    new_content = top + """
    <!-- Header -->
    <header class="relative pt-24 pb-12 lg:pt-32 lg:pb-16 overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold tracking-tight mb-6 text-white leading-tight">
                Stop Being Invisible. <br class="hidden lg:block" />
                <span class='text-transparent bg-clip-text bg-gradient-to-r from-primary via-red-500 to-rose-400 inline-block drop-shadow-lg pb-2'>Dominate Local Search</span>
                with SEO Services in Jamestown, NY.
            </h1>
            <p class="mt-4 max-w-3xl mx-auto text-lg md:text-xl text-gray-400 mb-8 leading-relaxed px-4">
                Building a beautiful website is only half the battle. If your customers can't find you on Google, your competitors are winning. We bridge the gap between "having a website" and "having a business that grows."
            </p>
            <a href="#audit-form"
                class="inline-flex items-center justify-center px-8 py-4 bg-primary text-white font-bold rounded-2xl hover:bg-primary-hover transition-all text-lg shadow-[0_0_20px_rgba(127,29,29,0.3)] hover:-translate-y-1">
                Get My Free SEO Audit <span
                    class="material-symbols-outlined ml-3 transform group-hover:translate-x-1">arrow_forward</span>
            </a>
        </div>
    </header>

    <!-- Main Content -->
    <main class="relative z-10 pb-24">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-24">
            
            <!-- Three Pillars Section -->
            <section>
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-extrabold text-white mb-6">Our Proven SEO Strategy for New York Businesses</h2>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <!-- Pillar 1 -->
                    <div class="glass-panel rounded-3xl p-8 hover:-translate-y-1 transition-transform cursor-default relative overflow-hidden group">
                        <div class="w-14 h-14 rounded-2xl bg-primary/20 text-primary flex items-center justify-center mb-6">
                            <span class="material-symbols-outlined text-3xl">build</span>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-4">Pillar 1: Technical SEO</h3>
                        <p class="text-gray-400 font-light text-sm leading-relaxed">
                            We ensure Google's "spiders" can crawl and index your site without errors. This includes fixing site speed, mobile responsiveness, and secure (HTTPS) protocols.
                        </p>
                    </div>

                    <!-- Pillar 2 -->
                    <div class="glass-panel rounded-3xl p-8 hover:-translate-y-1 transition-transform cursor-default relative overflow-hidden group">
                        <div class="w-14 h-14 rounded-2xl bg-primary/20 text-primary flex items-center justify-center mb-6">
                            <span class="material-symbols-outlined text-3xl">find_in_page</span>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-4">Pillar 2: On-Page Optimization</h3>
                        <p class="text-gray-400 font-light text-sm leading-relaxed">
                            We optimize every page of your site with high-value keywords, strategic headers, and engaging content that tells Google exactly why you’re the authority in your niche.
                        </p>
                    </div>

                    <!-- Pillar 3 -->
                    <div class="glass-panel rounded-3xl p-8 hover:-translate-y-1 transition-transform cursor-default relative overflow-hidden group">
                        <div class="w-14 h-14 rounded-2xl bg-primary/20 text-primary flex items-center justify-center mb-6">
                            <span class="material-symbols-outlined text-3xl">map</span>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-4">Pillar 3: Local SEO & Google Maps</h3>
                        <p class="text-gray-400 font-light text-sm leading-relaxed">
                            Most of your customers are right in your backyard. We optimize your Google Business Profile to ensure you show up in the "Map Pack" when people search for services "near me."
                        </p>
                    </div>
                </div>
            </section>

            <!-- The Click Media Edge -->
            <section class="glass-panel rounded-3xl p-8 lg:p-16 relative overflow-hidden">
                <div class="absolute -top-40 -right-40 w-96 h-96 bg-primary opacity-5 rounded-full blur-3xl pointer-events-none"></div>
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                    <div>
                        <h2 class="text-3xl lg:text-4xl font-extrabold text-white mb-6">Why Choose Us? The Power of Visual SEO.</h2>
                        <p class="text-gray-400 mb-6 font-light text-lg leading-relaxed">
                            Unlike "text-only" agencies, we leverage our background in Professional Photography and Videography. Google loves rich media. We optimize your images and YouTube content to ensure you appear not just in text results, but in Image and Video searches too. This creates a "multi-channel" presence that your competitors simply can't match.
                        </p>
                    </div>
                    <div class="rounded-3xl overflow-hidden shadow-2xl border border-white/10 group">
                        <div class="relative w-full h-80">
                            <img src="images/sun-seekers.webp" alt="Visual SEO Optimization" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
                            <div class="absolute bottom-6 left-6 right-6">
                                <span class="bg-primary text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider mb-3 inline-block">Visual Impact</span>
                                <h3 class="text-white text-xl font-bold">Optimized Media Drives Traffic</h3>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- FAQ & Audit Section Container -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
                
                <!-- FAQ -->
                <section>
                    <h2 class="text-3xl font-extrabold text-white mb-8">Frequently Asked Questions</h2>
                    <div class="space-y-6">
                        <div class="glass-panel rounded-2xl p-6">
                            <h3 class="text-xl font-bold text-white mb-3 flex items-start">
                                <span class="material-symbols-outlined text-primary mr-3 mt-0.5">help</span>
                                How long does SEO take?
                            </h3>
                            <p class="text-gray-400 font-light text-base leading-relaxed pl-9">
                                SEO is a marathon, not a sprint. While some technical fixes show immediate results, most businesses see significant growth in 3–6 months of consistent strategy.
                            </p>
                        </div>
                        <div class="glass-panel rounded-2xl p-6">
                            <h3 class="text-xl font-bold text-white mb-3 flex items-start">
                                <span class="material-symbols-outlined text-primary mr-3 mt-0.5">help</span>
                                Can you guarantee Page 1?
                            </h3>
                            <p class="text-gray-400 font-light text-base leading-relaxed pl-9">
                                No ethical agency can guarantee a #1 spot (since Google owns the algorithm), but we can guarantee a significant increase in your visibility and high-quality traffic.
                            </p>
                        </div>
                    </div>
                </section>

                <!-- PDF Download Form -->
                <section id="audit-form" class="glass-panel rounded-3xl p-8 lg:p-10 relative overflow-hidden outline outline-1 outline-primary/30">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-primary/10 rounded-bl-full pointer-events-none"></div>
                    <h2 class="text-2xl md:text-3xl font-extrabold text-white mb-4">The 10-Point SEO Checklist</h2>
                    <p class="text-gray-400 font-light mb-8 text-sm md:text-base">
                        Is your website invisible to Jamestown customers? Download our free, beautifully designed PDF checklist to find out. We'll show you exactly what's holding you back.
                    </p>
                    
                    <form action="https://formsubmit.co/rob@clickmediaandmarketing.com" method="POST" class="space-y-5">
                        <input type="hidden" name="_subject" value="New Request for SEO Audit PDF!">
                        <input type="hidden" name="_template" value="table">
                        <!-- Redirect directly to the PDF file on success -->
                        <input type="hidden" name="_next" value="https://www.clickmediaandmarketing.com/seo-audit.pdf">
                        <input type="hidden" name="_captcha" value="false">

                        <div>
                            <label for="name" class="block text-sm font-medium text-gray-300 mb-2">Your Name</label>
                            <input name="name" id="name" required type="text"
                                class="w-full bg-black/40 border border-white/10 rounded-xl px-5 py-3 text-white focus:outline-none focus:border-primary focus:bg-black/60 transition-all placeholder-gray-500"
                                placeholder="John Doe" />
                        </div>
                        <div>
                            <label for="email" class="block text-sm font-medium text-gray-300 mb-2">Email Address</label>
                            <input name="email" id="email" required type="email"
                                class="w-full bg-black/40 border border-white/10 rounded-xl px-5 py-3 text-white focus:outline-none focus:border-primary focus:bg-black/60 transition-all placeholder-gray-500"
                                placeholder="john@example.com" />
                        </div>
                        
                        <button type="submit"
                            class="w-full mt-4 bg-primary hover:bg-primary-hover text-white font-bold py-4 px-6 rounded-xl transition-all duration-300 shadow-[0_0_20px_rgba(127,29,29,0.3)] hover:shadow-[0_0_30px_rgba(127,29,29,0.5)] flex items-center justify-center text-lg">
                            <span class="material-symbols-outlined mr-2">download</span>
                            Download My Free SEO Audit
                        </button>
                    </form>
                    <p class="text-center text-xs text-gray-500 mt-4">We respect your privacy. No spam, ever.</p>
                </section>

            </div>
        </div>
    </main>
""" + bottom
    
    with open('/Volumes/Speedy Disk/click-media-site/seo.html', 'w', encoding='utf-8') as out:
        out.write(new_content)
    print("Created seo.html")
