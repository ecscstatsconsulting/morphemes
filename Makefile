.PHONY: all

define HEADER
                                            ,,
  `7MMM.     ,MMF'                         `7MM
   MMMb    dPMM                             MM
   M YM   ,M MM  ,pW"Wq.`7Mb,od8 `7MMpdMAo. MMpMMMb.  .gP"Ya `7MMpMMMb.pMMMb.  .gP"Ya  ,pP"Ybd
   M  Mb  M' MM 6W'   `Wb MM' "'   MM   `Wb MM    MM ,M'   Yb  MM    MM    MM ,M'   Yb 8I   `"
   M  YM.P'  MM 8M     M8 MM       MM    M8 MM    MM 8M""""""  MM    MM    MM 8M"""""" `YMMMa.
   M  `YM'   MM YA.   ,A9 MM       MM   ,AP MM    MM YM.    ,  MM    MM    MM YM.    , L.   I8
 .JML. `'  .JMML.`Ybmd9'.JMML.     MMbmmd'.JMML  JMML.`Mbmmd'.JMML  JMML  JMML.`Mbmmd' M9mmmP'
                                   MM
                                 .JMML.

  Authors: Enkeleda Çuko & Paul Warren
endef
export HEADER

_header:
	@clear
	@echo "$$HEADER"

_install:
	python setup.py install

_test:
	@echo
	@echo ================= RUNNING TESTS =================
	@python setup.py -q nosetests -s

info: _header
install: _header _install
test: _header _test