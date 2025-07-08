set -eux 

cd ~/RedHat/ostree

rm -rf ~/RedHat/ostree/usr

./autogen.sh
./configure --prefix=/home/pragyan/RedHat/ostree/usr
make
make install DESTDIR=/home/pragyan/RedHat/ostree/usr

scp -r ./usr core@bootc-only:
