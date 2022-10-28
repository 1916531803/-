%Harrison
img1=imread("1.png")
img2=imread("2.png")
img1_ycbcr = rgb2ycbcr(img1)
img2_ycbcr = rgb2ycbcr(img2)
C= imsubtract(img1_ycbcr,img2_ycbcr)
C=abs(img1_ycbcr(:,:,1)-img2_ycbcr(:,:,1))
imshow(C)
colormap(jet)
colorbar
caxis([0,10])
