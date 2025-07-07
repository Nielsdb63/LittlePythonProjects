import random
import numpy as np
import sys
import itertools
import time

start = time.time()

bombs, nrows, ncols = input('How many bombs, rows, columns? (3/3/3) ' )
bombs = int(bombs)
nrows = int(nrows)
ncols = int(ncols)
openedcells = []

def makeField2(subset):
  bombsCoords= [((x)//ncols,(x)%ncols) for x in list(subset)]
     
  field = {}
  allneighbors = []

  for i in bombsCoords:
    field[i] = 9
    neighbors = getNeighborFields(i[0], i[1])
    for i in neighbors:
      allneighbors.append(i)
  
  for i in allneighbors:
    if i not in field:
      field[i] = 0
    
  for i in allneighbors:
    if field[i] != 9:
      field[i] += 1
  
  return field

def fieldList():
  x = 0
  fieldlist = []
  stuff = range(nrows*ncols)
  for subset in itertools.combinations(stuff, bombs):
    field = makeField2(subset)
    fieldlist.append(field)
    x += 1
  return fieldlist

def getNoNeighborBombs(row,column,field):
    if field[row][column]==9:
        return 9
    
    sum=0
    neighbors=getNeighborFields(row,column)
    for (i,j) in neighbors:
      if field[i,j]==9:
          sum+=1     
  
    return sum

def getNeighborFields(row,column):
    neighbors= []
    rows = nrows - 1
    cols = ncols - 1
    
    if row!=0:
        neighbors.append((row-1,column))
        if column!=0:
            neighbors.append((row-1,column-1))
        if column!=cols:
            neighbors.append((row-1,column+1))
    
    if row!=rows:
        neighbors.append((row+1,column))
        if column!=0:
            neighbors.append((row+1,column-1))
        if column!=cols:
            neighbors.append((row+1,column+1))
            
    if column!=0:
        neighbors.append((row,column-1))
    
    if column!=cols:
        neighbors.append((row,column+1))
    
    return neighbors

def makeField():
    ntotal = nrows * ncols
    
    bombsPlaces= random.sample(range(ntotal),bombs)
    bombsCoords= [((x-1)//ncols,(x-1)%ncols) for x in bombsPlaces]
    field= np.zeros((nrows,ncols),dtype=int)
    
    for (i,j) in bombsCoords:
        field[i][j]=9
    
    for i in range(nrows):
        for j in range(ncols):
            field[i][j]= getNoNeighborBombs(i,j,field)
        
    return field

def Play(chosencell, fieldlist): 
    field= makeField()
    openedcells = chosencell[1]
    chosencell = chosencell[0]
    visible= np.ones((nrows,ncols),dtype=int)*10
    cellsleft=ncols*nrows
    print(visible)
    while cellsleft != bombs:
      cellsleft = 0
      row= chosencell[0][0]
      column= chosencell[0][1]

      inter = openCell(row,column,field,visible,fieldlist, openedcells)

      visible = inter[0]
      fieldlist = inter[1]
      openedcells = inter[2]
      
      inter2 = chance(fieldlist, openedcells)
      chosencell = inter2[0]
      openedcells = inter2[1]

      for i in visible:
        for j in i:
          if j == 10:
            cellsleft += 1
    x = 0
    print("End game")

def chance(fieldlist, openedcells):
  ntotal = nrows*ncols
  x = 0
  dictcount = {}
  while x < ntotal:
    dictcount[x//ncols,x%ncols] = 0
    x += 1
 
  listcount = []
  
  for i in fieldlist:
      for j in i:
        if i[j] == 9:
          dictcount[j] += 1

  dictcount = sorted(dictcount.items(), key=lambda x: x[1], reverse=False)

  possiblecells = []

  for i in dictcount:
    if i[0] not in openedcells:
      possiblecells.append(i)

  for i in possiblecells:
    if i[1] == possiblecells[0][1]:
      listcount.append(i[0])
 
  chosencell = random.sample(listcount,1)
  openedcells.append(chosencell[0])

  return chosencell, openedcells

def openCell(row,column,field,visible,fieldlist, openedcells):
    if field[row][column] == 9:
      print("Found a bomb!")
      sys.exit()
    
    if field[row][column] == 0:
      inter = iszero(row, column, field, visible, fieldlist, openedcells)


    else:
      visible[row][column] = field[row][column]
      fieldlist = fieldsleft(row, column, visible, fieldlist)
      openedcells.append((row, column))
      inter = [visible, fieldlist, openedcells]

    print(visible)
     

    return inter

def iszero(row, column, field, visible, fieldlist, openedcells):
  visible[row][column] = field[row][column]
  openedcells.append((row, column))
  fieldlist = fieldsleft(row, column, visible, fieldlist)

  zerolist = allzeros(row, column, field)
  for i in zerolist:
    visible[i[0]][i[1]] = field[i[0]][i[1]]
    fieldlist = fieldsleft(i[0], i[1], visible, fieldlist)
    openedcells.append((i[0], i[1]))
   
  return visible, fieldlist, openedcells

def allzeros(row, column, field):
  unchecked = getNeighborFields(row, column)
  zerolist = []
  while len(unchecked) != 0:
    row = unchecked[-1][0]
    column = unchecked[-1][1]
    if field[row][column] == 0:
        neighbors = getNeighborFields(row, column)
        for i in neighbors:
          if i not in zerolist:
            unchecked.append(i)
        unchecked.remove((row, column))
        zerolist.append((row, column))
    else:
        unchecked.remove((row, column))
        zerolist.append((row, column))
  zerolist = list(set(zerolist))
  return zerolist

def fieldsleft(row, column, visible, fieldlist):
  for i in range(len(fieldlist)):
    if visible[row][column] == 0:
      for j in fieldlist[i]:
        if j == (row, column):
          fieldlist[i] = 0
  
    else:
      if (row, column) in fieldlist[i].keys():
        if fieldlist[i][row, column] != visible[row][column]:
          fieldlist[i] = 0
      else:
        fieldlist[i] = 0
  
  fieldlist = [x for x in fieldlist if x!=0]
  return fieldlist

fieldlist = fieldList()

Play(chance(fieldlist, openedcells), fieldlist)

end = time.time()

print(end - start)