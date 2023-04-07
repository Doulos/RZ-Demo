all: sample_app_resnet50_img.cpp
	${CXX} -std=c++14 sample_app_resnet50_img.cpp \
	-lpthread -O2 -ldl ${LDFLAGS} -o sample_app_resnet50_img

clean:
	rm -rf *.o sample_app_resnet50_img
