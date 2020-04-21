const gulp = require("gulp");
const sass  = require("gulp-sass");
const sassGlob = require('gulp-sass-glob');
const plumber = require('gulp-plumber');
const notify  = require('gulp-notify');
const autoprefixer = require('autoprefixer');
const postcss = require('gulp-postcss')


const paths = {
    styles: {
        src: "./scss/**/*.scss",
        dest: "./css/"
    }
};

function styles() {
    return gulp.src(paths.styles.src)
        .pipe(sassGlob())
        .pipe(plumber({errorHandler: notify.onError('<%= error.message %>')}))
        .pipe(sass({ outputStyle: "expanded" }).on('error', sass.logError))
        .pipe(postcss([ autoprefixer() ]))
        .pipe(gulp.dest(paths.styles.dest));
}

function watch() {
    gulp.watch(paths.styles.src, styles);
}

exports.styles = styles
exports.watch = watch
exports.default = watch;
