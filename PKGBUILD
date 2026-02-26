pkgname=qsearch
pkgver=0.1
pkgrel=1
pkgdesc="Tiny quick search CLI"
arch=('x86_64')
license=('MIT')
depends=('python')
source=()
sha256sums=()

build() {
  cd "$startdir"
  ./build.sh
}

package() {
  cd "$startdir"

  install -Dm755 "$startdir/qsearch.pyz" \
    "$pkgdir/usr/bin/qsearch"
}