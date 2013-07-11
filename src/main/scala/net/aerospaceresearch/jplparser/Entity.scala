/*
 * Copyright (c) 2013 Elmar Athmer
 *
 * This file is part of SolarSystemGrandTour.
 *
 * SolarSystemGrandTour is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * SolarSystemGrandTour is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with SolarSystemGrandTour.  If not, see <http://www.gnu.org/licenses/>.
 */

package net.aerospaceresearch.jplparser

class Entity(val id: Int,
           startingLocation: Int,
           numberOfCoefficients: Int,
           numberOfCompleteSets: Int,
           completeRecords: List[BigDecimal],
           recordsPerInterval: Int
) {
  val numberOfPolynoms = if(id == 11) 2 else 3
  private val startingIndex = startingLocation - 3

  /**
   * List of Records specific for this entity
   */
  lazy val records: List[BigDecimal] = {
    // how many items of an interval belong to this Entity
    val myRecordsPerInterval = numberOfCoefficients * numberOfPolynoms * numberOfCompleteSets

    def recordsIter(completeRecords: List[BigDecimal], collectedRecords: List[BigDecimal]): List[BigDecimal] = {
      if(completeRecords.isEmpty) collectedRecords
      else recordsIter(
        completeRecords.drop(recordsPerInterval),
        collectedRecords ::: completeRecords.drop(startingIndex).take(myRecordsPerInterval)
      )
    }

    recordsIter(completeRecords, Nil)
  }
}
