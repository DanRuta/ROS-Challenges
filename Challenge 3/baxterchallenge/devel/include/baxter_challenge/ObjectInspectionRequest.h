// Generated by gencpp from file baxter_challenge/ObjectInspectionRequest.msg
// DO NOT EDIT!


#ifndef BAXTER_CHALLENGE_MESSAGE_OBJECTINSPECTIONREQUEST_H
#define BAXTER_CHALLENGE_MESSAGE_OBJECTINSPECTIONREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace baxter_challenge
{
template <class ContainerAllocator>
struct ObjectInspectionRequest_
{
  typedef ObjectInspectionRequest_<ContainerAllocator> Type;

  ObjectInspectionRequest_()
    {
    }
  ObjectInspectionRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ObjectInspectionRequest_

typedef ::baxter_challenge::ObjectInspectionRequest_<std::allocator<void> > ObjectInspectionRequest;

typedef boost::shared_ptr< ::baxter_challenge::ObjectInspectionRequest > ObjectInspectionRequestPtr;
typedef boost::shared_ptr< ::baxter_challenge::ObjectInspectionRequest const> ObjectInspectionRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace baxter_challenge

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'baxter_challenge': ['/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "baxter_challenge/ObjectInspectionRequest";
  }

  static const char* value(const ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
";
  }

  static const char* value(const ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ObjectInspectionRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::baxter_challenge::ObjectInspectionRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // BAXTER_CHALLENGE_MESSAGE_OBJECTINSPECTIONREQUEST_H