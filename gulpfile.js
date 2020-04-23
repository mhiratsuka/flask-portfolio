const gulp = require("gulp");
const sass  = require("gulp-sass");
const sassGlob = require('gulp-sass-glob');
const plumber = require('gulp-plumber');
const notify  = require('gulp-notify');
const autoprefixer = require('autoprefixer');
const postcss = require('gulp-postcss')
const browserSync = require('browser-sync').create();
const exec = require('child_process').exec;


const paths = {
    styles: {
        src: "./myportfolio/static/scss/**/*.scss",
        dest: "./myportfolio/static/css/"
    },
    htmls: {
        src: "./myportfolio/templates/**/*.html"
    }
};

function runServer(done) {
    exec('python run.py');
    done();
}

function browserReloadFunc(done) {
    browserSync.reload();
    done();
}

function browserSyncFunc(done) {
    browserSync.init({
        proxy: "127.0.0.1:5000",
        port: 8888
      });
    done();
}

function styles() {
    return gulp.src(paths.styles.src)
        .pipe(sassGlob())
        .pipe(plumber({errorHandler: notify.onError('<%= error.message %>')}))
        .pipe(sass({ outputStyle: "expanded" }).on('error', sass.logError))
        .pipe(postcss([ autoprefixer() ]))
        .pipe(gulp.dest(paths.styles.dest));
}

function watchFunc() {
    gulp.watch(paths.styles.src, styles);
    gulp.watch([paths.styles.src, paths.htmls.src], gulp.series('browserReloadFunc'));
}

const watch = gulp.parallel(watchFunc, runServer, browserSyncFunc);


exports.runServer = runServer;
exports.browserReloadFunc = browserReloadFunc;
exports.browserSyncFunc = browserSyncFunc;
exports.styles = styles;
exports.watchFunc = watchFunc;
exports.default = watch;
