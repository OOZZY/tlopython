import math

class Statistics:
  def __init__(self):
    self._size = 0
    self._sum = None
    self._mean = None
    self._min = None
    self._max = None
    self._range = None
    self._sumsquares = None
    self._meansquares = None
    self._variance = None
    self._stddeviation = None

  def add(self, num):
    self._size += 1
    if self._size == 1:
      self._sum = num
      self._mean = num
      self._min = num
      self._max = num
      self._range = 0
      self._sumsquares = num * num
      self._meansquares = self._sumsquares
      self._variance = 0
      self._stddeviation = 0
    else:
      self._sum += num
      self._mean = self._sum / self._size
      if self._min > num:
        self._min = num
      if self._max < num:
        self._max = num
      self._range = self._max - self._min
      self._sumsquares += num * num
      self._meansquares = self._sumsquares / self._size
      self._variance = self._meansquares - self._mean * self._mean
      self._stddeviation = math.sqrt(self._variance)

  @property
  def size(self):
    return self._size

  @property
  def sum(self):
    return self._sum

  @property
  def mean(self):
    return self._mean

  @property
  def min(self):
    return self._min

  @property
  def max(self):
    return self._max

  @property
  def range(self):
    return self._range

  @property
  def variance(self):
    return self._variance

  @property
  def stddeviation(self):
    return self._stddeviation

  def __repr__(self):
      return '{}: {}'.format(object.__repr__(self), self.__dict__)
