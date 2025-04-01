function load_static_content() {
    const header = document.getElementById("header")
    const footer = document.getElementById("footer")
    document.body.className = "bg-base-100"
    header.className = "navbar bg-base-200 shadow-sm fixed z-10"
    header.innerHTML = `
        <div class="navbar-start">
            <div class="dropdown">
                <div tabindex="0" role="button" class="btn btn-ghost btn-circle">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"></path>
                    </svg>
                </div>
                <ul tabindex="0" class="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow">
                    <li><a href="/">Homepage</a></li>
                    <li><a  href="https://jashandeep.co.uk" >Portfolio</a></li>
                    <li><a href="#footer">About</a></li>
                </ul>
            </div>
        </div>
        <div class="navbar-center">
            <a class="btn btn-ghost text-xl">Dashboard</a>
        </div>
        <div class="navbar-end px-5">
            <div class="flex items-center space-x-4 mt-4 md:mt-0">
                <div class="dropdown dropdown-end">
                    <label tabindex="0" class="btn btn-sm btn-outline border-gray-300 hover:bg-gray-100">
                        <i class="fas fa-download mr-2"></i> Export
                    </label>
                    <ul tabindex="0" class="dropdown-content menu p-2 shadow bg-white rounded-box w-40">
                        <li><a><i class="fas fa-file-pdf mr-2 text-red-500"></i> PDF</a></li>
                        <li><a><i class="fas fa-file-excel mr-2 text-green-600"></i> Excel</a></li>
                        <li><a><i class="fas fa-image mr-2 text-blue-500"></i> PNG</a></li>
                    </ul>
                </div>


                <div class="indicator">
                    <span class="indicator-item badge badge-primary badge-xs animate-pulse"></span>
                    <div class="dropdown dropdown-left">
                        <div tabindex="0" role="button" class="btn btn-sm">
                             <i class="fas fa-bell"></i>    
                        </div>
                        <ul tabindex="0" class="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow">
                            <li><a href="/">Homepage</a></li>
                            <li><a  href="https://jashandeep.co.uk" >Portfolio</a></li>
                            <li><a href="#footer">About</a></li>
                        </ul>
                    </div>
                
            </div>
        </div>`


    footer.className = "mt-20 pt-20 bg-base-200"
    footer.id = "footer"
    footer.innerHTML = `<div class="container mx-auto px-2 py-12 scale-[.8]">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div>
                <div class="flex items-center mb-4">
                    <svg width="40" height="40" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="mr-2">
                        <rect x="10" y="10" width="80" height="80" rx="5" fill="var(--primary)" />
                        <path d="M30 30 L70 30 L70 70 L30 70 Z" fill="white" />
                        <path d="M40 40 L60 40 L60 60 L40 60 Z" fill="var(--primary)" />
                    </svg>
                    <span class="text-lg font-semibold">Education-Employment Analytics</span>
                </div>
                <p class="text-sm text-gray-600 mb-4">Advanced analytical tools powered by Statistics Canada's
                    official data.</p>
                <div class="flex space-x-4">
                    <a><i class="fab fa-twitter text-lg"></i></a>
                    <a><i class="fab fa-linkedin-in text-lg"></i></a>
                    <a><i class="fab fa-github text-lg"></i></a>
                </div>
            </div>
            <div class="grid">
                <h3 class="footer-title">Data Resources</h3>
                <a class="link link-hover">Dataset Documentation</a>
                <a class="link link-hover">API Access</a>
                <a class="link link-hover">Methodology</a>
                <a class="link link-hover">Release Calendar</a>
            </div>
            <div class="grid">
                <h3 class="footer-title">Support</h3>
                <a class="link link-hover">Help Center</a>
                <a class="link link-hover">Training Webinars</a>
                <a class="link link-hover">User Guides</a>
                <a class="link link-hover">Contact Research Team</a>
            </div>
            <div class="grid">
                <h3 class="footer-title">Legal</h3>
                <a class="link link-hover">Open Government License</a>
                <a class="link link-hover">Privacy Policy</a>
                <a class="link link-hover">Accessibility</a>
                <a class="link link-hover">Terms of Service</a>
            </div>
        </div>
    </div>
</footer>`


}

setTimeout(() => {
    load_static_content()
}, 300);