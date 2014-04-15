package net.aerospaceresearch.test.utils

import org.scalatest.FunSuite
import org.scalatest.Matchers._
import net.aerospaceresearch.utils.SiConverter

/**
 * Created by elmar on 21.08.13.
 */
class SiConverterSpec extends FunSuite {

  test("time conversion") {
    val oneDayInSeconds = 24 * 60 * 60
    assert(oneDayInSeconds === SiConverter.fromDay(1))
  }

  test("length conversion") {
    assert(1000 === SiConverter.fromKm(1))
  }

  test("velocity conversion") {
    SiConverter.fromKmPerDay(30000).toDouble should be (347.2 +- 0.03)
  }

}
