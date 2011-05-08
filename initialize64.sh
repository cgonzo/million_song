export SJAR=/usr/lib/hadoop/contrib/streaming/hadoop-streaming-0.20.2-CDH3B4.jar
cp /mnt/data/ssh/config .ssh/config
git clone git://github.com/cgonzo/million_song.git
export HDF5_DIR=/mnt/data/hdf5_64/
export LD_LIBRARY_PATH=/mnt/data/hdf5_64/lib
apt-get remove -y cython
cd /mnt/data/installers/Cython-0.13/
python setup.py install
cd ../numexpr-1.4.2
python setup.py install
cd ../tables-2.2.1
python setup.py install
cp /mnt/data/bash_aliases ~/.bash_aliases
cd ~/million_song

