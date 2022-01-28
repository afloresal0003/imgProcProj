import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math



# this makes image look better on a macbook pro
def imageshow(img, dpi=200):
    if dpi > 0:
        F = plt.gcf()
        F.set_dpi(dpi)
    plt.imshow(img)


def rgb_ints_example():
    '''should produce red,purple,green squares
    on the diagonal, over a black background'''
    # RGB indexes
    red,green,blue = range(3)
    # img array 
    # all zeros = black pixels
    # shape: (150 rows, 150 cols, 3 colors)
    img = np.zeros((150,150,3), dtype=np.uint8)
    for x in range(50):
        for y in range(50):
            # red pixels
            img[x,y,red] = 255
            # purple pixels
            # set all 3 color components
            img[x+50, y+50,:] = (128, 0, 128)
            # green pixels
            img[x+100,y+100,green] = 255
    return img

# returns a new pattern that contains only the red, green or blue channel of the image. 
def onechannel(pattern, rgb):
  # Create pattern copy
  newPattern = np.copy(pattern)
  # Possible rgb channels 
  channels = [0,1,2]
  for channel in channels:
    if channel == rgb:
      # Keep 
      continue
    else:
      # Turn to black pixel
      newPattern[:,:,channel] = 0.0
  # Give back the one-channel pattern
  return newPattern


# swaps colors given image and permuation
def permutecolorchannels(img, perm):
  # Create pattern copy
  newPattern = np.copy(img)
  possibleCombinations = [[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
  for permu in possibleCombinations:
    # Special case 1
    if perm == [1,2,0]:
      newPattern[:,:,[0,1,2]] = newPattern[:,:,[2,0,1]]
      break
    # Special case 2
    elif perm == [2,0,1]:
      newPattern[:,:,[0,1,2]] = newPattern[:,:,[1,2,0]]
      break
    # Rest of the perms
    elif perm == permu:
      newPattern[:,:,[0,1,2]] = newPattern[:,:,permu]
      break
  # Give back the corrected pattern
  return newPattern

# returns a decrypted image.
def decrypt(image,key):
  # Create image copy
  realImg = np.copy(image)
  for x in range(len(key)):
    # Convert by channel
      realImg[:,x,0] = realImg[:,x,0]^key[x]
      realImg[:,x,1] = realImg[:,x,1]^key[x]
      realImg[:,x,2] = realImg[:,x,2]^key[x]
  return realImg

# main function 
def main():
    # To control display speed of the image
    pauseTime = 3

    patternImg = plt.imread('pattern.png')
    imageshow(patternImg)

    # Part 1
    plt.imshow(onechannel(patternImg, 0))
    plt.pause(pauseTime)
    plt.imshow(onechannel(patternImg,1))
    plt.pause(pauseTime)

    # Part 2
    plt.imshow(permutecolorchannels(patternImg,[1,0,2]))
    plt.pause(pauseTime)
    plt.imshow(permutecolorchannels(patternImg,[2,0,1]))
    plt.pause(pauseTime)

    permColImg = plt.imread('permcolors.jpg')
    plt.imshow(permutecolorchannels(permColImg,[1,2,0]))
    plt.pause(pauseTime)

    # Part 3
    secretImg = plt.imread('secret.bmp')
    decryptKey = np.load('key.npy')
    plt.imshow(decrypt(secretImg,decryptKey))
    plt.pause(pauseTime)

main()