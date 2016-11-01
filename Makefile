VIRTUOSO_BINARY = virtuoso-opensource/virtuoso/install/bin/virtuoso-t
HOST = elba.informatik.uni-freiburg.de
URL_PREFIX = freebase-qa/data

download-data:
	echo "Downloading data dependencies."
	echo "Downloading and extracting Aqqu data..."
	mkdir -p data/learning_cache; mkdir -p data/model-dir; cd data; wget "http://$(HOST)/$(URL_PREFIX)/data.tar.gz"; tar xvfz data.tar.gz
	echo "Downloading and extracting virtuoso index of Freebase..."
	wget "http://$(HOST)/$(URL_PREFIX)/virtuoso.tar.gz"; tar xvfz virtuoso.tar.gz

download:
	mkdir -p data/learning_cache; mkdir -p data/model-dir; cd data; wget "http://$(HOST)/$(URL_PREFIX)/data.tar.gz"; tar xvfz data.tar.gz

install-virtuoso:
	@echo "Installing virtuoso. Make sure you have all prerequisites installed (bison, flex etc.)."
	git clone https://github.com/openlink/virtuoso-opensource.git
	cd virtuoso-opensource; git checkout stable/7; ./autogen.sh
	cd virtuoso-opensource; ./configure --prefix=$$(pwd)/virtuoso/install
	cd virtuoso-opensource; make -j; make install
	@echo "Installation finished."

start-parser:
	cd corenlp-frontend; ant dist; ant run

start-virtuoso:
	$(VIRTUOSO_BINARY) -f +configfile virtuoso-db/virtuoso.ini
