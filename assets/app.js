function createGitHubLink() {
    const githubIcon = `
        <svg xmlns="http://www.w3.org/2000/svg" 
             width="26" 
             height="26" 
             fill="currentColor" 
             class="bi bi-github" 
             viewBox="0 0 16 16"
             aria-hidden="true">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"/>
        </svg>`;

    return `
        <a href="https://github.com/jayd719/CP321-finalproject1#"
           target="_blank" 
           rel="noopener noreferrer"
           aria-label="View project on GitHub">
            ${githubIcon}
            <span class="pl-4">GitHub</span>
        </a>`;
}

function createPortfolioLink() {
    const portfolioIcon = `
        <img src="https://jayd719.github.io/staticfiles/j.png" 
             alt="Portfolio icon" 
             width="26" 
             height="26">`;

    return `
        <a href="https://jashandeep.co.uk"
           target="_blank" 
           rel="noopener noreferrer"
           aria-label="View my portfolio">
            ${portfolioIcon}
            <span class="pl-4">Portfolio</span>
        </a>`;
}

function load_static_content() {
    const header = document.createElement("div")
    const footer = document.getElementById("footer")

    document.body.prepend(header)

    document.documentElement.setAttribute("data-theme", "light");

    header.className = "navbar bg-base-200 shadow-sm fixed z-10"
    header.innerHTML = `
        <div class="navbar-start">
            <div class="dropdown">
                <div tabindex="0" role="button" class="btn btn-ghost btn-circle">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"></path>
                    </svg>
                </div>
                <ul tabindex="0" class="menu menu-sm dropdown-content rounded-box z-1 mt-3 w-52 p-2 bg-base-300 gap-5">
                    <li>${createGitHubLink()}</li>
                    <li>${createPortfolioLink()}</li>
                </ul>
            </div>
        </div>
        <div class="navbar-center">
            <a class="btn btn-ghost text-xl">Dashboard</a>
        </div>
        <div class="navbar-end px-5">
            <div class="flex items-center space-x-4 mt-4 md:mt-0">
                <div class="dropdown dropdown-end">
                    <label tabindex="0" class="btn btn-outline hover:bg-gray-700 hover:text-white">
                        <i class="fas fa-download mr-2"></i> Export
                    </label>
                    <ul tabindex="0" class="dropdown-content menu p-2 shadow  rounded-box w-40 bg-base-200 border border-base-300 border-2">
                        <li><a id="actionbutton" onclick="actionButton();"><i class="fas fa-file-pdf mr-2 text-red-500"></i> PDF</a></li>
                        <li><a onclick="actionButton();"><i class="fas fa-file-excel mr-2 text-green-600"></i> Excel</a></li>
                        <li><a onclick="actionButton();"><i class="fas fa-image mr-2 text-blue-500"></i> PNG</a></li>
                    </ul>
                </div>


                <div class="indicator">
                    <span class="indicator-item badge badge-primary badge-xs animate-pulse"></span>
                    <div class="dropdown dropdown-left">
                        <div tabindex="0" role="button" class="btn btn-outline hover:bg-gray-700 hover:text-white">
                             <i class="fas fa-bell"></i>    
                        </div>
                        <ul tabindex="0" class="menu menu-sm dropdown-content rounded-box z-1 mt-3 w-52 p-2 bg-base-300 gap-5">
                             <li>${createGitHubLink()}</li>
                            <li>${createPortfolioLink()}</li>
                        </ul>
                    </div>
                
            </div>
        </div>`




}


load_static_content()
