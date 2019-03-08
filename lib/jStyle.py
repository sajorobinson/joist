jStyle = """/* JOIST STYLES */

/* DOCUMENT STYLES */

html, body {
    margin: 0;
    padding: 0;
    font-size: 18px;
    line-height: 1.5em;
    font-family: 'Open Sans', Arial, sans-serif;
    color: #333;
}

/* SECTION STYLES */

.hero {
    background: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)), url(https://images.unsplash.com/photo-1470087167738-6aa485ff65dc?ixlib=rb-0.3.5&s=df0adf58c0dfbf59749b04fa7557ac97&auto=format&fit=crop&w=1351&q=80);
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    height: 75vh;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
}

#footer {
    position: absolute;
    background-color: #263238;
    margin: 0;
    color: white;
    width: 100%;
}

.nav {
    margin-bottom: 50px;
}

.oneColumnBigText {
    text-align: center;
    margin: 50px 0 0 0;
}

/* ROW STLYES */

#footer .row {
    align-items: flex-start;
}

.row {
    display: flex;
    align-items: center;
    justify-content: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 1em;
    flex-wrap: wrap;
}

/* COLUMN STYLES */

.column {
    width: 100%;
    flex: 1 0 20%;
}

.fullImageColumn {
    background: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)), url(https://images.unsplash.com/photo-1470087167738-6aa485ff65dc?ixlib=rb-0.3.5&s=df0adf58c0dfbf59749b04fa7557ac97&auto=format&fit=crop&w=1351&q=80);
    background-position: top left;
    background-attachment: fixed;
    background-size: cover;
    height: 500px;
    /* Fixed height for empty div */
}

.menu .row .column {
    flex: 1 0 25%;
}

/* MODULE STYLES */

.button {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100px;
    height: 50px;
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    text-decoration: none;
    margin: 0 auto;
}

.cta {
    text-align: center;
}

.ctaFigure, .portfolioFigure {
    margin-bottom: -25px;
}

figure {
    margin: 0;
}

.fullImageText .row .column .text {
    padding: 3em 1em 3em 3em;
}

hr {
    margin: 50px 150px 0 150px;
}

.textFullImage .row .column .text {
    padding: 3em 3em 3em 1em;
}

.module {
    padding: 1em;
}

.module * {
    max-width: 100%;
}

/* TYPOGRAPHY */

a {
    color: lightblue;
    text-decoration: none;
}

.bigText {
    text-align: center;
    font-size: 2em;
    line-height: 1.4em;
}

#footer ul {
    list-style-type: none;
    padding: 0;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Roboto', Arial, sans-serif;
}

.menuDescription {
    font-style: italic;
}

.menuPrice {
    font-weight: bold;
    font-size: 1.2em;
}

p+h1, p+h2, p+h3, p+h4, p+h5, p+h6 {
    margin-top: 2em;
}

.portfolioText {
    text-align: left;
}

.portfolioText .button {
    margin: initial;
}

/* MEDIA QUERIES */

@media only screen and (max-width: 800px) {
    /* MEDIA QUERY ROW STYLE */
    .row {
        flex-direction: column;
    }
    .textFullImage .row .column .text {
        padding: 1em;
    }
    .fullImageText .row .column .text {
        padding: 1em;
    }
}
"""

jCustomStyle = """/* CUSTOM JOIST STYLES */
"""

jNavStyle = """.luxbar-default{
    width:100%;
    position:relative;
    box-shadow:0 1px 3px rgba(0,0,0,0.12),0 1px 2px rgba(0,0,0,0.24)
}
.luxbar-static{
    box-shadow:0 1px 3px rgba(0,0,0,0.12),0 1px 2px rgba(0,0,0,0.24);
    width:100%;
    position:absolute;
    top:0;
    left:0
}
.luxbar-static .luxbar-checkbox:checked ~ .luxbar-menu{
    position:absolute
}
.luxbar-fixed{
    width:100%;
    position:fixed;
    top:0;
    left:0;
    z-index:1000;
    box-shadow:0 1px 3px rgba(0,0,0,0.12),0 1px 2px rgba(0,0,0,0.24)
}
.luxbar-fixed-bottom{
    width:100%;
    position:fixed;
    bottom:0;
    left:0;
    z-index:1000;
    box-shadow:0 1px 3px rgba(0,0,0,0.12),0 1px 2px rgba(0,0,0,0.24)
}
.luxbar-hamburger span,.luxbar-hamburger span::before,.luxbar-hamburger span::after{
    display:block;
    height:2px;
    width:26px;
    transition:0.6s ease
}
.luxbar-checkbox:checked ~ .luxbar-menu li .luxbar-hamburger span{
    background-color:transparent
}
.luxbar-checkbox:checked ~ .luxbar-menu li .luxbar-hamburger span::before,.luxbar-checkbox:checked ~ .luxbar-menu li .luxbar-hamburger span::after{
    margin-top:0
}
.luxbar-header{
    display:flex;
    flex-direction:row;
    justify-content:space-between;
    align-items:center;
    height:58px
}
.luxbar-menu-left .luxbar-navigation,.luxbar-menu-left .luxbar-header{
    justify-content:flex-start
}
.luxbar-menu-right .luxbar-hamburger{
    margin-left:auto
}
.luxbar-brand{
    font-size:1.6em;
    padding:18px 24px 18px 24px
}
.luxbar-menu{
    min-height:58px;
    transition:0.6s ease;
    width:100%
}
.luxbar-navigation{
    display:flex;
    flex-direction:column;
    list-style:none;
    padding-left:0;
    margin:0
}
.luxbar-menu a,.luxbar-item a{
    text-decoration:none;
    color:inherit;
    cursor:pointer
}
.luxbar-item{
    height:58px
}
.luxbar-item a{
    padding:18px 24px 18px 24px;
    display:block;
}
.luxbar-hamburger{
    padding:18px 24px 18px 24px;
    position:relative;
    cursor:pointer
}
.luxbar-hamburger span::before,.luxbar-hamburger span::after{
    content:'';
    position:absolute
}
.luxbar-hamburger span::before{
    margin-top:-8px
}
.luxbar-hamburger span::after{
    margin-top:8px
}
.luxbar-checkbox{
    display:none
}
.luxbar-checkbox:not(:checked) ~ .luxbar-menu{
    overflow:hidden;
    height:58px
}
.luxbar-checkbox:checked ~ .luxbar-menu{
    transition:height 0.6s ease;
    height:100vh;
    overflow:auto
}
.dropdown{
    position:relative;
    height:auto;
    min-height:58px
}
.dropdown:hover>ul{
    position:relative;
    display:block;
    min-width:100%
}
.dropdown>a::after{
    position:absolute;
    content:'';
    right:10px;
    top:25px;
    border-width:5px 5px 0;
    border-color:transparent;
    border-style:solid
}
.dropdown>ul{
    display:block;
    overflow-x:hidden;
    list-style:none;
    padding:0
}
.dropdown>ul .luxbar-item{
    min-width:100%;
    height:29px;
    padding:5px 10px 5px 40px
}
.dropdown>ul .luxbar-item a{
    min-height:29px;
    line-height:29px;
    padding:0
}
@media screen and (min-width: 800px){
    .luxbar-navigation{
        flex-flow:row;
        justify-content:flex-end
    }
    .luxbar-hamburger{
        display:none
    }
    .luxbar-checkbox:not(:checked) ~ .luxbar-menu{
        overflow:visible
    }
    .luxbar-checkbox:checked ~ .luxbar-menu{
        height:58px
    }
    .luxbar-menu .luxbar-item{
        border-top:0
    }
    .luxbar-menu-right .luxbar-header{
        margin-right:auto
    }
    .dropdown{
        height:58px
    }
    .dropdown:hover>ul{
        position:absolute;
        left:0;
        top:58px;
        padding:0
    }
    .dropdown>ul{
        display:none
    }
    .dropdown>ul .luxbar-item{
        padding:5px 10px
    }
    .dropdown>ul .luxbar-item a{
        white-space:nowrap
    }
}
.luxbar-checkbox:checked+.luxbar-menu .luxbar-hamburger-doublespin span::before{
    transform:rotate(225deg)
}
.luxbar-checkbox:checked+.luxbar-menu .luxbar-hamburger-doublespin span::after{
    transform:rotate(-225deg)
}
.luxbar-checkbox:checked+.luxbar-menu .luxbar-hamburger-spin span::before{
    transform:rotate(45deg)
}
.luxbar-checkbox:checked+.luxbar-menu .luxbar-hamburger-spin span::after{
    transform:rotate(-45deg)
}
.luxbar-menu-dark,.luxbar-menu-dark .dropdown ul{
    background-color:#212121;
    color:#fff
}
.luxbar-menu-dark .active,.luxbar-menu-dark .luxbar-item:hover{
    background-color:#424242
}
.luxbar-menu-dark .luxbar-hamburger span,.luxbar-menu-dark .luxbar-hamburger span::before,.luxbar-menu-dark .luxbar-hamburger span::after{
    background-color:#fff
}
.luxbar-menu-light,.luxbar-menu-light .dropdown ul{
    background-color:#e0e0e0;
    color:#212121
}
.luxbar-menu-light .active,.luxbar-menu-light .luxbar-item:hover{
    background-color:#bdbdbd
}
.luxbar-menu-light .luxbar-hamburger span,.luxbar-menu-light .luxbar-hamburger span::before,.luxbar-menu-light .luxbar-hamburger span::after{
    background-color:#212121
}
.luxbar-menu-material-red,.luxbar-menu-material-red .dropdown ul{
    background-color:#b71c1c;
    color:#fff
}
.luxbar-menu-material-red .active,.luxbar-menu-material-red .luxbar-item:hover{
    background-color:#c62828
}
.luxbar-menu-material-red .luxbar-hamburger span,.luxbar-menu-material-red .luxbar-hamburger span::before,.luxbar-menu-material-red .luxbar-hamburger span::after{
    background-color:#fff
}
.luxbar-menu-material-indigo,.luxbar-menu-material-indigo .dropdown ul{
    background-color:#1a237e;
    color:#fff
}
.luxbar-menu-material-indigo .active,.luxbar-menu-material-indigo .luxbar-item:hover{
    background-color:#283593
}
.luxbar-menu-material-indigo .luxbar-hamburger span,.luxbar-menu-material-indigo .luxbar-hamburger span::before,.luxbar-menu-material-indigo .luxbar-hamburger span::after{
    background-color:#fff
}
.luxbar-menu-material-green,.luxbar-menu-material-green .dropdown ul{
    background-color:#1b5e20;
    color:#fff
}
.luxbar-menu-material-green .active,.luxbar-menu-material-green .luxbar-item:hover{
    background-color:#2e7d32
}
.luxbar-menu-material-green .luxbar-hamburger span,.luxbar-menu-material-green .luxbar-hamburger span::before,.luxbar-menu-material-green .luxbar-hamburger span::after{
    background-color:#fff
}
.luxbar-menu-material-amber,.luxbar-menu-material-amber .dropdown ul{
    background-color:#ff6f00;
    color:#fff
}
.luxbar-menu-material-amber .active,.luxbar-menu-material-amber .luxbar-item:hover{
    background-color:#ff8f00
}
.luxbar-menu-material-amber .luxbar-hamburger span,.luxbar-menu-material-amber .luxbar-hamburger span::before,.luxbar-menu-material-amber .luxbar-hamburger span::after{
    background-color:#fff
}
.luxbar-menu-material-brown,.luxbar-menu-material-brown .dropdown ul{
    background-color:#3e2723;
    color:#fff
}
.luxbar-menu-material-brown .active,.luxbar-menu-material-brown .luxbar-item:hover{
    background-color:#4e342e
}
.luxbar-menu-material-brown .luxbar-hamburger span,.luxbar-menu-material-brown .luxbar-hamburger span::before,.luxbar-menu-material-brown .luxbar-hamburger span::after{
    background-color:#fff
}
.luxbar-menu-material-bluegrey,.luxbar-menu-material-bluegrey .dropdown ul{
    background-color:#263238;
    color:#fff
}
.luxbar-menu-material-bluegrey .active,.luxbar-menu-material-bluegrey .luxbar-item:hover{
    background-color:#37474f
}
.luxbar-menu-material-bluegrey .luxbar-hamburger span,.luxbar-menu-material-bluegrey .luxbar-hamburger span::before,.luxbar-menu-material-bluegrey .luxbar-hamburger span::after{
    background-color:#fff
}
.luxbar-menu-material-cyan,.luxbar-menu-material-cyan .dropdown ul{
    background-color:#006064;
    color:#fff
}
.luxbar-menu-material-cyan .active,.luxbar-menu-material-cyan .luxbar-item:hover{
    background-color:#00838f
}
.luxbar-menu-material-cyan .luxbar-hamburger span,.luxbar-menu-material-cyan .luxbar-hamburger span::before,.luxbar-menu-material-cyan .luxbar-hamburger span::after{
    background-color:#fff
}
/*# sourceMappingURL=luxbar.min.css.map */

/* CUSTOM STYLES */

.luxbar-item a{
    padding:15px 24px 18px 24px;
    display:block;
}
"""
